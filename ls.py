#!/usr/bin/python
import os;
import sys;

#arglist = str(sys.argv)
#arglist=sys.argv		// sys.argv is the command line list where the first tuple is always the script itself
#print arglist[0]
#print arglist[1]

targetPath= sys.argv[1]
print "list all the directories and files under the root path: targetPath"
for root, dir, file in os.walk(targetPath):
	print root
	print dir
	print file
