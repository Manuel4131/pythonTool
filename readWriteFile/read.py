#!/usr/bin/python

filename=raw_input("Please enter the file name to be accessed:  ")
mode=raw_input("Please select the mode, w:overwrite, r:readonly, r+:read+write, a:append data to filename:  ")
try:
    f = open(filename,mode)
except IOError as e:
    print "I/O error {0}, {1}".format(e.errno, e.stderror)

# Test while
for line in f:
	print line,
f.close()
