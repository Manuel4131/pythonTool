#!/usr/bin/python

#import os;
#import sys;
#import glob;

import os, sys, time, inspect, operator;
from datetime import datetime;
startime= datetime.now()

k=float(1024)
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

# targetPath=sys.argv[1]
# ls(targetPath
# val=sys.argv[1]
# translateUnit(val)

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
	if args.showHiddenItem == 'n':			# without 'a'
		items = removeHiddenFile_(items)

	if args.nameOnly == 'y':				# without 'l'
		for item in items:
			print (('%s') % (item.itemName + '\t'))
	elif args.nameOnly == 'n':				# with 'l'
		# Set time attribute:
		for i in items:
		 	i.setmtime()	

	 	if args.sortByTime == 'y':			# with 't'
	 		if args.reverseOrder == 'y':	# with 'r' or not
	 			items.sort(key=operator.attrgetter("mtime"),reverse= True)
	 		else:
	 			items.sort(key=operator.attrgetter("mtime"),reverse= False)

#final print
 	for item in items:
 		if item.filetype == 1:				# type{0,1,2}, {dir, file, others}
			printFile_(item)
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
	showHiddenItem, nameOnly, sortByTime, sortByDescOrder, humanRead, reverseOrder= 'y', 'y', 'n', 'n', 'n', 'n'
	# initValue = showHiddenItem + deli + nameOnly + deli + sortByTime + deli	+ sortByDescOrder + deli + humanRead + deli	+ reverseOrder
	if "a" not in option:
		showHiddenItem='n'
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


class itemInfo(object):
	"""docstring for itemInfo"""
	def __init__(self,rootDir=None, itemName=None, mtime=None):
		super(itemInfo, self).__init__()
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


	# __cmp__

def removeHiddenFile_(list):
	newItemList=[]
	newItemList= [x for x in list if not x.itemName.startswith('.')]
	return newItemList

def createItems(path):
	itemsList=[]
	items = os.listdir(path)
	abspath = os.path.abspath(path)	
	for i in items:
		item = itemInfo(abspath, i)		# Ticket 2
		itemsList.append(item)	
	return itemsList


ls(sys.argv)
print "Passed time:	", datetime.now() -startime





	