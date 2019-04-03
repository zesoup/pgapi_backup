
class backupsolution:
    """Virtual Parent for all Backups
    Highlevel-API:
        @list_backups( cluster_identifier=None,  backup_identifier=None)
        @take_backup(kind,cluster_identifier=None, options=None)
        @setup(cluster_identifier=None,  options=None)
        @check(cluster_identifier=None,  options=None)

    Childs should override:
    
        @list_backups(self,cluster_identifier=None,  backup_identifier=None)
        @_take_full_backup(self,cluster_identifier=None, options=None)
        @_take_incremental_backup(self,cluster_identifier=None, options=None)
        @_take_logical_backup(self,cluster_identifier=None, options=None)
    """

    def list_backups(self, cluster_identifier=None,  backup_identifier=None):
        """
            { "Clusteridentifier: { "Backupidentifier": {},..}, ..}
            In the event of zero existing backups a cluster will be listed
            as toplevel in list_backups. Hence it is sufficient to have list_backups
            and omit a list_clusters function.
        """
        backupsolution._warn_not_implemented("list-backups")
    def setup(self, cluster_identifier=None,  backup_identifier=None):
        backupsolution._warn_not_implemented("setup")
    def check(self, cluster_identifier=None,  backup_identifier=None):
        backupsolution._warn_not_implemented("check")

    def take_backup(self, kind='full', cluster_identifier=None,  backup_identifier=None, options=None):
        """Currently 3 Kinds of backups are supported:
            * full - full physical
            * incremental - incremental physical
            * logical - logical
        """
        if kind=='full':
            self._take_full_backup(cluster_identifier, options)
        elif kind== 'incremental':
            self._take_incremental_backup(cluster_identifier, options)
        elif kind== 'logical':
            self._take_logical_backup(cluster_identifier, options)
    
    def _take_full_backup(self, cluster_identifier=None, options=None):
        backupsolution._warn_not_implemented('FULL-BACKUP')

    def _take_incremental_backup(self, cluster_identifier=None, options=None):
        backupsolution._warn_not_implemented('INCREMENTAL-BACKUP')
    
    def _take_logical_backup(self, cluster_identifier=None, options=None):
        backupsolution._warn_not_implemented('LOGICAL-BACKUP')

    @staticmethod
    def _warn_not_implemented(service):
        raise Exception(service+" is not supported")