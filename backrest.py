from backup import backup
from logging import debug, log, info, warning, critical
from subprocess import Popen, std

class backrest( backup ):
    def __init__(self,  cluster_version, cluster_name ):
        super(  ).__init__(cluster_version, cluster_name)
        debug("Backrest Initialized")

    def  list_backups(self):
        pass

    def _take_full_backup(self):
        pass
    def _take_incremental_backup(self):
        pass


if __name__=='__main__':    
    from logging import getLogger,DEBUG
    getLogger(__name__).setLevel(DEBUG)

    br=backrest('10','main')
    br.list_backups()

    br.take_backup()
    br.take_backup(kind='logical')
    br.take_backup(kind='incremental')
