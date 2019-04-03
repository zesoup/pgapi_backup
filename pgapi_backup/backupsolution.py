
class backupsolution:
    """Virtual Parent for all Backups
    Highlevel-API:
        @list_backups( cluster_identifier=None,  backupidentifier=None)
        @list_clusters()
        @take_backup(kind,cluster_identifier=None)
        @setup(cluster_identifier=None,  backupidentifier=None)
        @check(cluster_identifier=None,  backupidentifier=None)

    Childs should override:
    
        @list_backups(self,cluster_identifier=None,  backupidentifier=None)
        @_take_full_backup(self,cluster_identifier=None)
        @_take_incremental_backup(self,cluster_identifier=None)
        @_take_logical_backup(self,cluster_identifier=None)
    """

    def list_clusters(self):
        """
            { "Clusteridentifier: { "Backupidentifier": {},..}, ..}
        """
        backupsolution._warn_not_implemented("list-clusters")
    def list_backups(self, cluster_identifier=None,  backupidentifier=None):
        backupsolution._warn_not_implemented("list-backups")
    def setup(self, cluster_identifier=None,  backupidentifier=None):
        backupsolution._warn_not_implemented("setup")
    def check(self, cluster_identifier=None,  backupidentifier=None):
        backupsolution._warn_not_implemented("check")

    def take_backup(self, kind='full', cluster_identifier=None,  backupidentifier=None):
        """Currently 3 Kinds of backups are supported:
            * full - full physical
            * incremental - incremental physical
            * logical - logical
        """
        if kind=='full':
            self._take_full_backup()
        elif kind== 'incremental':
            self._take_incremental_backup()
        elif kind== 'logical':
            self._take_logical_backup()
    
    def _take_full_backup(self, cluster_identifier=None):
        backupsolution._warn_not_implemented('FULL-BACKUP')

    def _take_incremental_backup(self, cluster_identifier=None):
        backupsolution._warn_not_implemented('INCREMENTAL-BACKUP')
    
    def _take_logical_backup(self, cluster_identifier=None):
        backupsolution._warn_not_implemented('LOGICAL-BACKUP')

    @staticmethod
    def _warn_not_implemented(service):
        raise Exception(service+" is not supported")