#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys, time, inspect, operator; 
from datetime import datetime;


K=1024.

def getPermission(file, type):
	perSt=""
	if type:
		perSt='d'
	else :
		perSt='-'        
	perNum=oct(os.stat(file).st_mode)[-3:]
	t=('--x','-w-','-wx','r--','r-x','rw-','rwx')
	for i in range(0,3):
		perSt+=t[int(perNum[i]) -1]
	return perSt


def translateUnit(bits):
	bits=float(bits)
	d=0
	units=('B','K','M','G','T','P')
	while bits >= 1024:			
		bits/=K
		d=d+1
	bits=round(bits,2)
	return repr(bits) + units[0]

	
def getDirSize(targetPath):		
	totalSize=0
	for rootDir, subDir, subFile in os.walk(targetPath):
		for file in subFile:
			totalSize += os.path.getsize(os.path.join(rootDir,file))
	return totalSize


def printFile(item):
	print (('%s') % (getPermission(item.targetPath,0) + '\t')), (('%s') % (item.itemName +'\t')), ( ('%s') % ( translateUnit(os.path.getsize(item.targetPath))) + '\t' ), ( ('%s') % ( time.ctime( item.mtime ) + '\t' ) )


def printDir(item):
 	print "{:>10} {:>10} {:>8} {:>20}".format(getPermission(item.targetPath,1), item.itemName + '/', translateUnit(getDirSize(item.targetPath)), time.ctime( item.mtime ))


def createAbspath(list):
	absPath = []
	i = 0
	while i < len(list):
		absPath.append( os.path.abspath(list[i]))
		i+=1
	return absPath

def printFormat(args, path):
	items =createItems(path)

	if not args.showHiddenItem:			
		items = removeHiddenFile(items)

	if args.nameOnly:				
		for item in items:
			print (('%s') % (item.itemName + '\t')),	
	elif not args.nameOnly:			
		for i in items:				
		 	i.setmtime()	

	 	if args.sortByTime:			# with 't'
	 		if args.reverseOrder:	# with 'r' or not
	 			items.sort(key=operator.attrgetter("mtime"),reverse= False)
	 		else:
	 			items.sort(key=operator.attrgetter("mtime"),reverse= True)

	 	for item in items:
	 		if item.filetype == 1:				# type{0,1,2}, {dir, file, others}
				printFile(item)
			elif item.filetype == 0:
				printDir(item)


def ls(argv):
	argvLength= len(argv)
# input format check and pass to corresponding function.
	if argv[1][0]=='-' and argvLength == 2:
		print "no target file"
		printFormat(setargument(argv[1]),'.')

	elif argv[1][0]=='-' and argvLength == 3:
		print "Target file"
	else:
		print "list file names only"


# Print main function
def setargument(option):
	showHiddenItem, nameOnly, sortByTime, = True, True, False  
	sortByDescOrder, humanRead, reverseOrder = False, False, False
	
	if "a" not in option:
		showHiddenItem=False
	
	showHiddenItem, nameOnly, sortByTime =  False, True, False
	humanRead, reverseOrder=  False, False 
	dic={}
	dic["showHiddenItem"]= True if 'a' in option else False
	if "l" in option:
		dic["nameOnly"] = False
		# Set relative attribute values:
		dic["sortByTime"]=True if "t" in option else False
		dic["humanRead"]=True if "h" in option else False
		dic["reverseOrder"]=True if "r" in option else False
	# Use dictionary instead.

	arg=Arg(**dic)
	return arg


class Arg(object):
	
	def __init__(self,showHiddenItem=False, nameOnly=False, sortByTime=False, reverseOrder=False, humanRead=False):
		self.showHiddenItem= showHiddenItem
		self.nameOnly = nameOnly
		self.sortByTime = sortByTime
		self.reverseOrder = reverseOrder
		self.humanRead = humanRead
		
	# print self.showHiddenItem		# Why can't I call the self.showHiddenItem value in class scope?
	def setVar(self,argvlist):
		showHiddenItem, nameOnly, sortByTime, reverseOrder, humanRead=argvlist.split(',')


class ItemInfo(object):			# First char in class name should be uppercase.
	"""docstring for ItemInfo"""
	def __init__(self,rootDir=None, itemName=None, mtime=None):
		super(ItemInfo, self).__init__()
		self.rootDir= rootDir
		self.itemName= itemName
		self.mtime= mtime
		self.targetPath= os.path.join(self.rootDir, self.itemName)
		if(os.path.isfile(self.targetPath)):
			self.filetype = 1
		elif(os.path.isdir(self.targetPath)):
			self.filetype = 0
		else:
			self.filetype = 2
	def setmtime(self):
		self.mtime= os.path.getmtime(self.targetPath)


def removeHiddenFile_(fileList): # Avoid use keyword as variable name
	newItemList=[]
	newItemList= [x for x in fileList if not x.itemName.startswith('.')]

def removeHiddenFile(argList): # list is a default class name, ID/			highlight_
	newItemList=[]
	newItemList= [x for x in argList if not x.itemName.startswith('.')]
	return newItemList


def createItems(path):			
	itemsList=[]
	items = os.listdir(path)
	abspath = os.path.abspath(path)	
	for i in items:
		item = ItemInfo(abspath, i)
		itemsList.append(item)
	return itemsList

ls(sys.argv)
# print "Passed time:	", datetime.now() -startime


