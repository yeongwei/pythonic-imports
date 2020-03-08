#!/usr/bin/python

import sys

def printSysPaths(file):
	print(file + " -> " + ", ".join(sys.path))
