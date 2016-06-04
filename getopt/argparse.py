#!/usr/bin/python
import getopt
import sys


optpair,args =getopt.getopt(sys.argv[1:],"hl:t:")

for opt, optArg in optpair:
	
	if opt == '-h':
		print "file size"
	elif opt == '-l':
		print "File: " + optArg
	