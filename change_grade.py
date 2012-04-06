#!/usr/bin/env python

import re
from sys import stderr,stdout,argv

def grade_change(data, name, grade):
	toReturn = list()
	for line in data:
		app = line
		if re.search (name, line):
			app = re.sub ('[0-9]+', grade, line)
		toReturn.append(line)
	return toReturn

if __name__=='__main__':
	from sys import stdin, stdout, stderr, argv
	data = grade_change(stdin, argv[1], argv[2])
	for line in data:
		print line