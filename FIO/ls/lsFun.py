#!/usr/bin/python

#import os;
#import sys;
#import glob;

k=float(1024)
import os, sys, time;

def translateUnit(bits):
	bits=int(bits)
	d=0
	units=('B','K','M','G','T')
	while bits >= 1024:			
		bits/=k
		d=d+1
	return repr(bits) + units[0]
	# return 
	# print "bis are:", bits
	# print "degree is: ", units[d]
	
def getDirSize(targetPath):
	totalSize=0
	for rootDir, subDir, subFile in os.walk(targetPath):
		for file in subFile:
			totalSize += os.path.getsize(os.path.join(rootDir,file))
	return totalSize

def printFile(targetPath):
	print "{:>10} {:>8} {:>20}".format(targetPath, translateUnit(os.path.getsize(targetPath)), time.ctime(os.path.getatime(targetPath)))

def printDir(targetPath):
	print "{:>10} {:>8} {:>20}".format(targetPath, translateUnit(getDirSize(targetPath)), time.ctime(os.path.getatime(targetPath)))	
	
def ls(targetPath):	
	if os.path.isfile(targetPath):
		printFile(targetPath)
	elif os.path.isdir(targetPath):	
		printDir(targetPath)

targetPath=sys.argv[1]
ls(targetPath)
# val=sys.argv[1]
# translateUnit(val)

