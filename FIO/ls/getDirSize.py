#!/usr/bin/python

import os, sys;

rootPath = sys.argv[1]

totalSize=0;
for rootDir, subDir, subFile in os.walk(rootPath):
    for f in subFile:
        fObj = os.path.join(rootDir, f)
        print 'absolute path: {0}, size is {1}'.format(fObj, os.path.getsize(fObj))
        totalSize+=os.path.getsize(fObj)
        
print totalSize
