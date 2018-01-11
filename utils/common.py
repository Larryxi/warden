#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import shutil

def programEroor(message):
    print message
    sys.exit(1)

def checkRoot():
    if os.geteuid() != 0:
        programEroor("[!] The program must be started by root")

def checkDirectory(path):
    return os.path.isdir(path)

def makeDirectory(path):
    if not checkDirectory(path):
        os.makedirs(path)

def copyFile(src, dst):
    dst_path = os.path.dirname(dst)
    makeDirectory(dst_path)
    shutil.copy(src, dst)
