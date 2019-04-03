
class backup:
    """Virtual Parent for all Backups
    Highlevel-API:
        @list_backups()
        @take_backup(kind)
        @setup()
        @check()

    Childs should override:
    
        @list_backups(self)
        @_take_full_backup(self)
        @_take_incremental_backup(self)
        @_take_logical_backup(self)
    """
    def __init__(self, cluster_version, cluster_name):
        self.cluster_version = cluster_version
        self.cluster_name = cluster_name

    def list_backups(self):
        pass

    def take_backup(self, kind='full'):
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
    
    def _take_full_backup(self):
        backup._warn_not_implemented('FULL-BACKUP')

    def _take_incremental_backup(self):
        backup._warn_not_implemented('INCREMENTAL-BACKUP')
    
    def _take_logical_backup(self):
        backup._warn_not_implemented('LOGICAL-BACKUP')

    @staticmethod
    def _warn_not_implemented(service):
        raise Exception(service+" is not supported")