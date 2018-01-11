#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser

import utils.globalvar as g
from utils.common import checkDirectory
from utils.common import makeDirectory

def configFileParser(configFile):
    config = ConfigParser.ConfigParser()
    config.read(configFile)
    paths = []

    for k, v in config.items("watch"):
        if checkDirectory(v):
            paths.append(v)

    backup_path = config.get("backup", "path")
    makeDirectory(backup_path)
    g.setBackupPath(backup_path)

    return paths
