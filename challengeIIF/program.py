#!/usr/bin/env python3

import sys

# minimum mile
def milesMinimum(nTacos,calories):
	miles = 0
	for i in range(nTacos):
		miles += 2**i * calories[i]
	return miles

#main
if __name__ == '__main__':
	lines = [line.rstrip() for line in sys.stdin.readlines()]
	for i in range(0,len(lines),2):
		nTacos = int(lines[i])
		calories = [int(x) for x in lines[i+1].split(" ")]
		calories.sort(reverse=True)
		print(milesMinimum(nTacos,calories))
