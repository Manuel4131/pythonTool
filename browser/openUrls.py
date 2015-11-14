#!/usr/bin/python

import webbrowser;

list=['google','github']

for i in xrange(0,len(list)):
	try:
		webbrowser.open("http://www." + list[i] + ".com", 1)
	except Exception, e:
		raise 
	
	
