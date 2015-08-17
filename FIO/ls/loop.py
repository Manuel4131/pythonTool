#!/usr/bin/python
import sys
k=1024
oridata=sys.argv[1]
oridata=int(oridata)
d=0
degree=('KB','M','G')

while oridata / k >= 1:
    oridata/=k
    q=oridata
    d+=1

print "q is", q
print "d is", d

if d > 0:
	print "degree is", degree[d - 1]