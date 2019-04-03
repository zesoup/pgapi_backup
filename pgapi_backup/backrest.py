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

    def list_backups(self, cluster_identifier = None, backup_identifier = None):
        all_clusters =  self._list()
        if cluster_identifier:
            if cluster_identifier in all_clusters:
                out = all_clusters[cluster_identifier]
            else:
                raise Exception("Cluster does not exist")
        elif backup_identifier:
            raise Exception("Backupdetails not yet implemented")
              
        return out
        
    def _take_full_backup(self,cluster_identifier=None, options=None):
        pass
    def _take_incremental_backup(self, cluster_identifier=None, options=None):
        pass
    def setup(cluster_identifier=None,  options=None):
        pass
    def check(cluster_identifier=None,  options=None):
        pass
    
