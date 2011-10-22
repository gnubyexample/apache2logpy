#!/usr/bin/env python
"""
http://creativecommons.org/licenses/by-sa/2.0/uk/
http://identi.ca/gnubyexample
"""

import re
import fileinput

re_keepalive = re.compile('\042')
#re_keepalive = re.compile("\d")
#re_keepalive = re.compile("404")
#re_keepalive = re.compile('"\s[0-9]')

for line in fileinput.input():
	if (re_keepalive.search(line)):
		#print "matched..."
		numbers = re_keepalive.split(line)[2]
		keepalive = numbers.split()[-1]
		if int(keepalive) > 1:
			print numbers, re_keepalive.split(line)[3]
		else:
			print numbers
