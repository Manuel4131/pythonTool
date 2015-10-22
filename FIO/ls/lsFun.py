#!/usr/bin/python

#import os;
#import sys;
#import glob;
# from __future__ import print_function

import os, sys, time, inspect, operator; # ; against P8
from datetime import datetime;

# Use shell script 'time' instead!.  Built-in module called 

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
		bits/=k
		d=d+1

	bits=round(bits,2)
	return repr(bits) + units[0]
		# Function && Function 
	# more case: the item may contain '/''
	
def getDirSize(targetPath):		
	totalSize=0
	# print "targetPath", targetPath
	for rootDir, subDir, subFile in os.walk(targetPath):
		for file in subFile:
			totalSize += os.path.getsize(os.path.join(rootDir,file))
	return totalSize

# Change the api to have another argument: fileSize which is decieded by the attribute 'h'	
def printFile_(item):
	print (('%s') % (getPermission(item.targetPath,0) + '\t')), (('%s') % (item.itemName +'\t')), ( ('%s') % ( translateUnit(os.path.getsize(item.targetPath))) + '\t' ), ( ('%s') % ( time.ctime( item.mtime ) + '\t' ) )


def printDir_(item):
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
# Set the list element according the argument attribute	
	if args.showHiddenItem:			# without 'a'
		items = removeHiddenFile_(items)

	if args.nameOnly:				# without 'l'
		for item in items:
			print (('%s') % (item.itemName + '\t')),	
	elif args.nameOnly:				# with 'l'
		# Set time attribute:
		print 'l'
		for i in items:
		 	i.setmtime()	

	 	if args.sortByTime:			# with 't'
	 		if args.reverseOrder:	# with 'r' or not
	 			items.sort(key=operator.attrgetter("mtime"),reverse= True)
	 		else:
	 			items.sort(key=operator.attrgetter("mtime"),reverse= False)

	 	for item in items:
	 		if item.filetype == 1:				# type{0,1,2}, {dir, file, others}
				printFile_(item)
				print 1
			elif item.filetype == 0:
				printDir_(item)
	# elif args.nameOnly == 'n':
	# 	abspath = createAbspath(items)
	# 	for i in range(0, len(items)):
	# 		if os.path.isfile(abspath[i]):
	# 			printFile(abspath[i],items[i])
	# 		elif os.path.isdir(abspath[i]):
	# 			printDir(abspath[i],items[i])


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
	# itemList= os.listdir(target)	# Change itemList to object list
	deli=','
# use enum or dict instead, plz
	showHiddenItem, nameOnly, sortByTime, sortByDescOrder, humanRead, reverseOrder= True, True, False, False, False, False # True, False Why not?
	# line by line
	# initValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli	+ sortByDescOrder + deli + humanRead + deli	+ reverseOrder
	if "a" not in option:
		showHiddenItem=False
	if "l" in option:
		nameOnly=False
		if "t" in option:
			sortByTime=True
			sortByDescOrder=True
		if "h" in option:
			humanRead=True			
		if "r" in option:
			reverseOrder=True
	# Use dictionary instead.
	# #opts={}
	# opts['reverse_Order'] = 'y' if 'r' in option else 'n'
	# opts['reverse_Order2'] = 'y' if 'r' in option else 'n'
	# arg = Args(**opts)
	# class Args(object):

	# 	def __init__(self, reverse_Order, reverse_Order2):
	# 		pass
	dic={}
	dic["showHiddenItem"] = showHiddenItem
	dic["nameOnly"] = nameOnly
	dic["sortByTime"] = sortByTime
	dic["sortByDescOrder"] = sortByDescOrder
	dic["reverseOrder"] = reverseOrder
	dic["humanRead"] = humanRead

 	# resultValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli + sortByDescOrder  + deli	+ reverseOrder + deli + humanRead # string 
	arg=Arg(**dic)
	return arg


class Arg(object):
	
	def __init__(self,showHiddenItem=False, nameOnly=False, sortByTime=False, sortByDescOrder=False, reverseOrder=False, humanRead=False):
		self.showHiddenItem= showHiddenItem
		self.nameOnly = nameOnly
		self.sortByTime = sortByTime
		self.sortByDescOrder = sortByDescOrder
		self.reverseOrder = reverseOrder
		self.humanRead = humanRead
		
		# self.showHiddenItem, self.nameOnly, self.sortByTime, self.sortByDescOrder, self.reverseOrder, self.humanRead=argvlist.split(',')	
	# print self.showHiddenItem		# Why can't I call the self.showHiddenItem value in class scope?
	def setVar(self,argvlist):
		showHiddenItem, nameOnly, sortByTime, sortByDescOrder, reverseOrder, humanRead=argvlist.split(',')


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


def removeHiddenFile_(list): # list is a default class name, ID/			highlight_
	newItemList=[]
	newItemList= [x for x in list if not x.itemName.startswith('.')]
	return newItemList


def createItems(path):
	itemsList=[]
	items = os.listdir(path)
	abspath = os.path.abspath(path)	
	for i in items:
		item = ItemInfo(abspath, i)		# Ticket 2
		itemsList.append(item)					# list 
	return itemsList


ls(sys.argv)
# print "Passed time:	", datetime.now() -startime
