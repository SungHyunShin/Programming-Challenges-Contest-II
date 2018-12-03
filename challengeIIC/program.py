#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys

#main
if __name__ == '__main__':
	lines = [line.rstrip() for line in sys.stdin.readlines()]
	for i in range(0,len(lines),2):
		print(lines[i])
		print(lines[i+1])
