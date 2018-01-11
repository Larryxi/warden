#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

from utils.common import checkRoot
from utils.watchfile import ArcWarden
from utils.cmdline import cmdLineParser
from utils.configfile import configFileParser

def main():
    checkRoot()
    options = cmdLineParser()
    paths = configFileParser(options.configfile)
    dogs = []

    for path in paths:
        dog = ArcWarden(path)
        dogs.append(dog)

    for dog in dogs:
        dog.start()

    try:  
        while True:  
            time.sleep(1)  
    except KeyboardInterrupt:
        for dog in dogs:  
            dog.stop()  
    
    for dog in dogs:
        dog.join()

if __name__ == "__main__":
    main()
