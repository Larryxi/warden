#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ArcConifg:
    backup_path = "/var/log/warden/backup"

def setBackupPath(path):
    ArcConifg.backup_path = path

def getBackupPath():
    return ArcConifg.backup_path
