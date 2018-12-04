#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys

def longestPerm(word1,word2):
	perm = []
	word2 = [x for x in word2]
	for char in word1:
		if char in word2:
			word2.remove(char)
			perm += char
	if perm:
		perm.sort()
		print("".join(perm))
	else:
		print()

#main
if __name__ == '__main__':
	lines = [line.rstrip() for line in sys.stdin.readlines()]
	for i in range(0,len(lines),2):
		longestPerm(lines[i],lines[i+1])
