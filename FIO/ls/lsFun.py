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

def printFormat(args, path):
	items = os.listdir(path)
	if args.showHiddenItem == 'n':
		items = removeHiddenFile(items)

	if args.nameOnly == 'y':
		for item in items:
			print ('%10s') % (item),


def ls(argv):
	argvLength= len(argv)
# input format check and pass to corresponding function.
	if argv[1][0]=='-' and argvLength == 2:
		print "no target file"
		printFormat( setargument(argv[1]),'.')

	elif argv[1][0]=='-' and argvLength == 3:
		print "Target file"
	else:
		print "list file names only"

# Print main function
def setargument(option):
	# itemList= os.listdir(target)	# Change itemList to object list
	deli=','
	# use enum or dict instead, plz
	showHiddenItem, nameOnly, sortByTime, sortByDescOrder, humanRead, reverseOrder= 'y', 'y', 'n', 'n', 'n', 'n'
	# initValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli	+ sortByDescOrder + deli + humanRead + deli	+ reverseOrder
	# arg=Arg(initValue)
	# print arg.humanRead
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
	
	resultValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli + sortByDescOrder  + deli	+ reverseOrder + deli + humanRead
	arg=Arg(resultValue)
	return arg

class Arg(object):

	command="ls"
	def __init__(self,argvlist):
		self.showHiddenItem, self.nameOnly, self.sortByTime, self.sortByDescOrder, self.reverseOrder, self.humanRead=argvlist.split(',')
	
	# print self.showHiddenItem		# Why can't I call the self.showHiddenItem value in class scope?
	def setVar(self,argvlist):
		showHiddenItem, nameOnly, sortByTime, sortByDescOrder, reverseOrder, humanRead=argvlist.split(',')

def removeHiddenFile(list):
	newList=[]
	newList[:]= [x for x in list if not x.startswith('.')]
	return newList

ls(sys.argv)




	