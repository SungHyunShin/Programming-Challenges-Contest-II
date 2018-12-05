#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys
import collections
import difflib
import copy

def isWordMorph(w1,w2):
	diff = 0
	for s in difflib.ndiff(w1,w2):
		if s[0] != ' ':
			diff += 1
	return diff == 2 and len(w1) == len(w2) or diff == 1 and len(w1) == len(w2)+1 or diff == 1 and len(w1)+1 == len(w2)


def buildedgeL(wordL):
	edgeL = []
	for i in range(len(wordL)):
		edgeL.append([0]*len(wordL))
	for i in range(len(wordL)):
		for j in range(i+1, len(wordL)):
			if isWordMorph(wordL[j],wordL[i]):
				edgeL[i][j] = 1
	return edgeL

def bfs(edgeL,v, end):

	
	frontier = []
	path = []
	path.append(v)
	frontier.append((v,path))
	all_paths = []
	while frontier:
		x = min(frontier,key=lambda t: len(t[1]))
		frontier.remove(x)
		v, path = x
		
		if v == end:
			all_paths.append(path)
			continue
		for i,u in enumerate(edgeL[v]):
			if u == 1:
				p = copy.deepcopy(path)
				p.append(i)
				frontier.append((i,p))
	return all_paths

#main
if __name__ == '__main__':
	wordL = [line.rstrip() for line in sys.stdin.readlines()]
	wordL.sort()
	#print(wordL)
	edgeL = buildedgeL(wordL)

	longestP = []
	paths = []
	for v in range(len(wordL)):
		for k in range(v, len(wordL)):
			curr = bfs(edgeL,v, k)
			if curr != []:
				for path in curr:
					paths.append(path)
	longest = 0
	final_path = []
	for path in paths:
		if len(path) > longest:
			longest = len(path)
			final_path = path
	print(longest)
	for i in sorted(final_path):
		print(wordL[i])
		
