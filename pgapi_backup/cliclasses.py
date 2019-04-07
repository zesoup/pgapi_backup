from subprocess import Popen, PIPE
from logging import warning, debug

from threading import Thread
from collections import deque
import json

from configparser import ConfigParser, DuplicateSectionError

background_tasks = []


class background_task(Thread):
    def __init__(self, proc):
        self.proc = proc
        background_tasks.append(self)

    def run(self):
        for line in self.proc.stdout:
            print(line)
            self.proc.poll()


class cli:
    @staticmethod
    def _run_cmd(cmd, blocking=True):
        debug("Executing: %s" % (str(cmd)))
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        if len(background_tasks) > 10:
            warning("More than 10 jobs active")
        if blocking == False:
            background_task(proc).run()
            return None
        else:
            proc.poll()
            return ([line.strip().decode('ascii') for line in proc.stdout], [line.strip().decode() for line in proc.stderr], proc.returncode)


class backrestconfig:
    def __init__(self):
        self.path = '/etc/pgbackrest.conf'
        self.config = ConfigParser()
        self.config.read(self.path)


    def flush(self):
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

    def add_cluster(self, stanza):
        debug(f"Adding Cluster {stanza}")
        try:
            self.config.add_section(stanza)
            self.flush()
        except DuplicateSectionError:
            warning(f"{stanza} allready exists as configsection")
        return True
    
    def delete_cluster(self, stanza):
        self.config.remove_section(stanza)
        self.flush()
    
    def add_key(self, stanza, key, value):
        debug(f"Adding Key {stanza} {key} {value}")
        self.config.set(stanza, key, value)
        self.flush()

    def as_dict(self):
        out = {}
        for section in self.config.sections():
            out[section] = {}
            for key in self.config[section]:
                out[section][key] = self.config[section][key]
        return out

    def dict_merge_into(self, target):
        conf_dict = self.as_dict()
        resultdict = {}
        for key in target:
            resultdict[key] = target[key]
        for key in conf_dict:
            if key in resultdict:
                resultdict[key] = {**conf_dict[key], **resultdict[key]}
            else:
                resultdict[key] = conf_dict[key]
        return resultdict


class backrest(cli):

    @staticmethod
    def info():
        (stdout, stderr, _) = cli._run_cmd(
            ["pgbackrest", "info", "--output=json"],  blocking=True)
        json_out = json.loads(''.join(stdout))

        return (json_out, stderr)
    @staticmethod
    def stanza_create(stanza):
        (stdout, stderr, rc) = cli._run_cmd(
            ["pgbackrest", "start", "--stanza", stanza, ],  blocking=True)
        (stdout, stderr, rc) = cli._run_cmd(
            ["pgbackrest", "stanza-create", "--stanza", stanza, ],  blocking=True)
        return (''.join(stdout), stderr, rc)

    @staticmethod
    def stanza_delete(stanza):
        (stdout, stderr, rc) = cli._run_cmd(
            ["pgbackrest", "stop", "--stanza", stanza, '--force'],  blocking=True)
        (stdout, stderr, rc) = cli._run_cmd(
            ["pgbackrest", "stanza-delete", "--stanza", stanza, '--force'],  blocking=True)
        return (''.join(stdout), stderr, rc)

    @staticmethod
    def backup(stanza):
        (stdout, stderr, rc) = cli._run_cmd(
            ["pgbackrest", "stanza-delete", "--stanza", stanza, ],  blocking=True)
        return (''.join(stdout), stderr, rc)
