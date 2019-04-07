#!/usr/bin/env python3

from pgapi_backup.backrest import *


def test_backrest_remove_cluster():
    assert True == backrest().remove_cluster('10-main')

def test_backrest_remove_cluster():
    assert True == backrest().add_cluster('10-main')

def test_backrest_listbackups_full():
    assert True == backrest().list_backups()

def test_backrest_listbackups_existing_cluster():
    assert True == backrest().list_backups(cluster_identifier='10-main')

def test_backrest_listbackups_nonexisting_cluster():
    assert False == backrest().list_backups(backup_identifier='1234')


