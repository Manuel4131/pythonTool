#!/usr/bin/python

import argparse

description0 = 'Enter the birthday in \
		\'year month day\' format and you\'ll get a magic number'
descrp1 = "Guess an integer number in [1, 100]"

arg_p = argparse.ArgumentParser(description= descrp1)
arg_p.add_argument("-g", help = "make a guess in [1,100]",
					 type = int)
arg_p.add_argument("--gender", help = "Are you female", action= 'store_true')


args = arg_p.parse_args()

if args.g == 48:
		print 'yes'
else:
		print 'Nie'

if args.gender:
    print "Hi, ^  ^"
else:
    print "bye"
