from pgapi_backup.backupsolution import backupsolution
from pgapi_backup.cliclasses import backrest as backrest_cli

from logging import debug, log, info, warning, critical

class backrest( backupsolution ):

    def  list_clusters(self):
        (stdout, stderr) = backrest_cli.info() 
        return [ line.split(': ')[-1] for line in stdout if "stanza: " in line ]

    def  list_backups(self, cluster_identifier=None,  backupidentifier=None):
        return {"a":1}

    def _take_full_backup(self,cluster_identifier=None):
        pass
    def _take_incremental_backup(self, cluster_identifier=None):
        pass


if __name__=='__main__':    
    from logging import getLogger,DEBUG
    getLogger(__name__).setLevel(DEBUG)

    br=backrest()
    br.list_backups()

    br.take_backup()
    br.take_backup(kind='logical')
    br.take_backup(kind='incremental')
