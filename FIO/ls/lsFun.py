#!/usr/bin/python

#import os;
#import sys;
#import glob;

k=float(1024)
import os, sys, time;

def getPermission(file):
	perSt=""
	if os.path.isdir(file):
		perSt='d'
	elif os.path.isfile(file):
		perSt='-'
        
	perNum=oct(os.stat(file).st_mode)[-3:]
	t=('--x','-w-','-wx','r--','r-x','rw-','rwx')
	for i in range(0,3):
		perSt+=t[int(perNum[i]) -1]
    

	return perSt

def translateUnit(bits):
	bits=float(bits)
	d=0
	units=('B','K','M','G','T')
	while bits >= 1024:			
		bits/=k
		d=d+1

	bits=round(bits,2)
	return repr(bits) + units[0]
	
def getDirSize(targetPath):
	totalSize=0
	for rootDir, subDir, subFile in os.walk(targetPath):
		for file in subFile:
			totalSize += os.path.getsize(os.path.join(rootDir,file))
	return totalSize

def printFile(targetPath):
	print "{:>10} {:>10} {:>8} {:>20}".format(getPermission(targetPath), targetPath, translateUnit(os.path.getsize(targetPath)), time.ctime(os.path.getatime(targetPath)))

def printDir(targetPath):
	print "{:>10} {:>10} {:>8} {:>20}".format(getPermission(targetPath),targetPath, translateUnit(getDirSize(targetPath)), time.ctime(os.path.getatime(targetPath)))	
	
# def ls(targetPath):
# 	if os.path.isfile(targetPath):
# 		printFile(targetPath)
# 	elif os.path.isdir(targetPath):
# 			printDir(item)

# targetPath=sys.argv[1]
# ls(targetPath
# val=sys.argv[1]
# translateUnit(val)

def printNameOnly(list):
		print "{:>4}".format()
	

def ls(argv):
	argvLength= len(argv)
# input format check and pass to corresponding function.
	if argv[1][0]=='-' and argvLength == 2:
		print "no target file"
		printOutput(argv[1], '.')
	elif argv[1][0]=='-' and argvLength == 3:
		print "Target file"
	else:
		print "list file names only"

# Print main function
def printOutput(option, target):
	itemList= os.listdir(target)	# Change itemList to object list
	
	showHiddenItem=True
	nameOnly=True
	sortByTime=False
	reverseOrder=False
	sortByDescOrder=False
	humanRead=False

	if "a" not in option:
		showHiddenItem=False
		# itemList= removeHiddenFile(itemList)
	if "l" in option:
		nameOnly=False
		if "t" in option:
			sortByDescOrder=True
		if "h" in option:
			humanRead=True
			
		if "r" in option:
			reverseOrder=True
	# print "nameOnly is: {0}", nameOnly
		argumentlist= 

def printResult():
	pass



def removeHiddenFile(list):
	newList=[]
	newList[:]= [x for x in list if not x.startswith('.')]
	return newList

class Argument:
	command="ls"
	def __init__(self, argumentlist):



ls(sys.argv)