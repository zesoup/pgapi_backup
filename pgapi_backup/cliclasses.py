from subprocess import Popen, PIPE
from logging import warning, debug

from threading import Thread
from collections import deque


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
    def _run_cmd(self, cmd, stream=False, blocking=True ):
        def poll_command( proc ):
            proc = Popen(cmd, stdout=PIPE )#, stderr=PIPE)
            if len(background_task) > 10:
                warning( "More than 10 jobs active")

            background_task( proc ).run()    



if __name__=='__main__':
        c=cli()
        i=["bash","test.sh"]
        c._run_cmd(cmd=i)
        import time

        for x in background_tasks:
            print(x.returncode)

        time.sleep(2)