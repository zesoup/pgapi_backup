from subprocess import Popen, PIPE
from logging import warning, debug

from threading import Thread
from collections import deque
import json

background_tasks = []

class background_task(Thread):
    def __init__(self, proc):
        self.proc=proc
        background_tasks.append(self)
    def run(self):
        for line in self.proc.stdout:
            print(line)
            self.proc.poll()

class cli:
    @staticmethod
    def _run_cmd(cmd, blocking=True ):
        debug("Executing: %s"%(str(cmd)) )
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        if len(background_tasks) > 10:
            warning( "More than 10 jobs active")
        if blocking==False:
            background_task( proc ).run()
            return None
        else:
            proc.poll()
            return ([line.strip().decode('ascii') for line in proc.stdout], [line.strip().decode() for line in proc.stderr], proc.returncode)

class backrest(cli):
    @staticmethod
    def info():
        (stdout, stderr, _) = cli._run_cmd( ["pgbackrest","info", "--output=json"],  blocking=True )
        return (json.loads(''.join(stdout) ) , stderr)

    def stanza_create(stanza, pg1path):
        assert( pg1path != None )
        (stdout, stderr, rc) = cli._run_cmd( ["pgbackrest","stanza-create","--stanza", stanza, "--pg1-path",pg1path ],  blocking=True )
        return ( ''.join(stdout ) , stderr, rc)

    def stanza_delete(stanza, pg1path):
        assert( pg1path != None )
        (stdout, stderr, rc) = cli._run_cmd( ["pgbackrest","stanza-delete","--stanza", stanza, "--pg1-path",pg1path, '--force' ],  blocking=True )
        return ( ''.join(stdout ) , stderr, rc)