#!/usr/bin/env python

import re
import fileinput
import string
from sys import stderr,stdout,argv,exit

def grad_change1(data, name, grade)
	for line in data:
		m = re.search (name, line)
		if m:
			print re.sub ('[%s]' % string.digits, grade, line)
	return (data)



from sys import stdin, stdout, stderr, argv

if __name__=='__main__':
	from sys import stdin, stdout, stderr, argv

	(data) = grade_change1(stdin, argv[1], argv[2])



