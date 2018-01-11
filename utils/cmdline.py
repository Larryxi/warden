#!/usr/bin/env python
# -*- coding:utf-8 -*-

import optparse

def cmdLineParser():
	usage = "usage: %prog [-c conifgfile]"
	parser = optparse.OptionParser(usage=usage)
	parser.add_option("-c", "--config",dest="configfile",
		              metavar="FILE", default="warden.conf",
		              help="config file to load")

	(options, args) = parser.parse_args()
	return options
