from pgapi_backup.backupsolution import backupsolution
from pgapi_backup.cliclasses import backrest as backrest_cli
from logging import debug, log, info, warning, critical

from flask_restful import reqparse

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
        out = all_clusters
        if cluster_identifier:
            if cluster_identifier in all_clusters:
                out = all_clusters[cluster_identifier]
            else:
                raise Exception("Cluster does not exist")
        elif backup_identifier:
            raise Exception("Backupdetails not yet implemented")
              
        return out
        
    def _take_full_backup(self,cluster_identifier=None, ):
        pass
    def _take_incremental_backup(self, cluster_identifier=None, ):
        pass
    def add_cluster(self,cluster_identifier=None):
        parser = reqparse.RequestParser() 
        parser.add_argument("pg1-path", type=str, default=None)
        args = parser.parse_args(strict=True)
        out = backrest_cli.stanza_create(cluster_identifier, args['pg1-path'] )
        return {"stdout": out[0], "stderr": out[1]}

    def remove_cluster(self,cluster_identifier=None):
        parser = reqparse.RequestParser() 
        parser.add_argument("pg1-path", type=str, default=None)
        args = parser.parse_args(strict=True)
        out = backrest_cli.stanza_delete(cluster_identifier, args['pg1-path'])
        return {"stdout": out[0], "stderr": out[1]}

        
    def check(self, cluster_identifier=None,  ):
        pass
    
