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
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        if len(background_tasks) > 10:
            warning( "More than 10 jobs active")
        if blocking==False:
            background_task( proc ).run()
            return None
        else:
            return ([line.strip().decode('ascii') for line in proc.stdout], [line.strip().decode() for line in proc.stderr])

class backrest(cli):
    @staticmethod
    def info():
        (stdout, stderr) = cli._run_cmd( ["pgbackrest","info", "--output=json"],  blocking=True )
        return (json.loads(''.join(stdout) ) , stderr)
