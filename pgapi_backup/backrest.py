from pgapi_backup.backupsolution import backupsolution
from pgapi_backup.cliclasses import backrest as backrest_cli

from logging import debug, log, info, warning, critical

class backrest( backupsolution ):

    def  _list(self):
        (stdout_json, stderr) = backrest_cli.info()
        schema_corrected_output = {}
        for cluster in stdout_json:
            schema_corrected_output[ cluster['name'] ] = {}
            for backup in cluster['backup']:
                schema_corrected_output[ cluster['name'] ][ backup['label']] = backup
        return schema_corrected_output

    def  list_backups(self, cluster_identifier = None):
        all_clusters =  self._list()
        out = all_clusters[cluster_identifier] if cluster_identifier in all_clusters else all_clusters
        return out
        

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
