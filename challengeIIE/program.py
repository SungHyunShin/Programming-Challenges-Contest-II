#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys

# find minimum amount of hops
def minimumHop(start,end):
	hopD = 1
	hopC = 0
	current = start
	distance = end - current
	while current < end:
		hopC +=1
		current += hopD
		distance = end - current
		# if hop can be increased
		if distance >= sum(range(hopD+2)):
			hopD +=1
		# if hop needs to be decreased
		elif distance < sum(range(hopD+1)):
			hopD -=1
	# print output
	print(start,"->",end,"takes",hopC,"hops")

# main
if __name__ == '__main__':
	for line in sys.stdin.readlines():
		start, end = ([int(x) for x in line.rstrip().split(" ")])
		minimumHop(start,end)
