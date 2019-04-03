
from flask import jsonify, abort
from flask_restful import Resource, reqparse
import logging

from pgapi_backup.backup import *

class _Backup(Resource):

    def get(self, section=None):
        """
        """
        logging.info("GET Request for Backups, section=\"%s\"", section)

        #system_info = get_system_info(section)
        out = {"rc":1}
        return jsonify(out)#system_info)

def registerHandlers(api):
    api.add_resource(_Backup, '/backup/', endpoint="backup")
    api.add_resource(_Backup, '/backup/<string:version>/<string:name>', endpoint="backup_version_name")
