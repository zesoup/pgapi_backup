
from flask import jsonify, abort
from flask_restful import Resource, reqparse
import logging

from pgapi_backup.backrest import backrest as backup
"""
    Backupimplementations share a common API, which makes them plugable via their
    parent 'backup'.

    For the moment, it is not decided when and where the decision for the actual
    implementation is done.

    For the time beeing, this is hardcoded to backrest due to it's use in elephant-shed
    and the lack of alternatives.

    As it is propably done with a configdriven factory, using a rewired backup directly
    should do no harm.
    """

class _Backup(Resource):
    def get(self):
        logging.info("GET Request for Backups")
        backups = backup().list_clusters()
        return jsonify(backups)

class _BackupCluster(Resource):
    def get(self, clusteridentifier):
        logging.info("GET Request for Backups")
        backups = backup().list_backups()# in hindsight, we should do something different here
        return jsonify(backups)

    def put(self, clusteridentifier):
        logging.info("GET Request for Backups")
        backups = backup().list_backups()# in hindsight, we should do something different here
        return jsonify(backups)

    def delete(self, clusteridentifier):
        logging.info("GET Request for Backups")
        backups = backup().list_backups()# in hindsight, we should do something different here
        return jsonify(backups)






def registerHandlers(api):
    api.add_resource(_Backup, '/backup/', endpoint="backup")
    api.add_resource(_BackupCluster, '/backup/<string:clusteridentifier>', endpoint="backup_clusteridentifier")
    #api.add_resource(_Backup, '/backup/<string:clusteridentifier>/<string:identifier>', endpoint="backup_clusteridentifier")