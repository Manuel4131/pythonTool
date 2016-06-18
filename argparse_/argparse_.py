#/usr/bin/python

import argparse

parser=argparse.ArgumentParser(description='ls')
parser.add_argument('-l', action='append', default=[], dest='ll', help='no way!')

result=parser.parse_args()


#for i in range(len(result)):
#    print result[i]
