#!/usr/bin/env python
import os
def test():

	p = os.popen('./a.out 12345','r')
	while 1:
		line = p.readline();
		if '' == line:
			break;
		print line
if __name__== '__main__':
	test()
