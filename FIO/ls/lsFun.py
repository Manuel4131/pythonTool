#!/usr/bin/python

#import os;
#import sys;
#import glob;
import os, sys, time;

def getDirSize(targetPath):
	totalSize=0
	for rootDir, subDir, subFile in os.walk(targetPath):
		for file in subFile:
			totalSize += os.path.getsize(os.path.join(rootDir,file))
	return totalSize

def printFile(targetPath):
	print "{:>10} {:>8} {:>20}".format(targetPath, os.path.getsize(targetPath), time.ctime(os.path.getatime(targetPath)))

def printDir(targetPath):
	print "{:>10} {:>8} {:>20}".format(targetPath, getDirSize(targetPath), time.ctime(os.path.getatime(targetPath)))	
	
def ls(targetPath):	
	if os.path.isfile(targetPath):
		printFile(targetPath)
	elif os.path.isdir(targetPath):	
		printDir(targetPath)

targetPath=sys.argv[1]
ls(targetPath)
