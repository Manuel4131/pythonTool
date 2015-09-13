#!/usr/bin/python

#import os;
#import sys;
#import glob;

import os, sys, time;

k=float(1024)
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
	deli=','
	# use enum or dict instead, plz
	showHiddenItem, nameOnly, sortByTime, sortByDescOrder, humanRead, reverseOrder= 'y', 'y', 'n', 'n', 'n', 'n'
	initValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli	+ sortByDescOrder + deli + humanRead + deli	+ reverseOrder
	arg=Arg(initValue)
	print arg.humanRead
	if "a" not in option:
		showHiddenItem='n'
		# itemList= removeHiddenFile(itemList)
	if "l" in option:
		nameOnly='n'
		if "t" in option:
			sortByTime='y'
			sortByDescOrder='y'
		if "h" in option:
			humanRead='y'
			
		if "r" in option:
			reverseOrder='y'
	
	resultValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli	+ sortByDescOrder + deli + humanRead + deli	+ reverseOrder
	# arglist= showHiddenItem + deli + nameOnly;

# def printResult(showHiddenItem, nameOnly, sortByTime, reverseOrder, reverseOrder, sortByTime, humanRead):
# 	pass 



def removeHiddenFile(list):
	newList=[]
	newList[:]= [x for x in list if not x.startswith('.')]
	return newList

class Arg(object):

	command="ls"
	def __init__(self,argvlist):
		# self.showHiddenItem, self.nameOnly, self.sortByTime=showHiddenItem, nameOnly, sortByTime
		# self.reverseOrder, self.sortByDescOrder, self.humanRead=reverseOrder,sortByDescOrder,humanRead
		self.showHiddenItem, self.nameOnly, self.sortByTime, self.sortByDescOrder, self.reverseOrder, self.humanRead=argvlist.split(',')
	
	# print self.showHiddenItem		# Why can't I call the self.showHiddenItem value in class scope?
	


ls(sys.argv)
