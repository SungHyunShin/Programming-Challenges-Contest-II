#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys
import collections
import difflib

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
		for j in range(i+1,len(wordL)):
			if isWordMorph(wordL[j],wordL[i]):
				edgeL[i][j] = 1
	return edgeL

def bfs(edgeL,v):
	longestP = []
	
	frontier = []
	longestPath = []
	marked = set()
	path = []
	path.append(v)
	frontier.append((v,path))

	while frontier:
		x = min(frontier,key=lambda t: len(t[1]))
		frontier.remove(x)
		v,path = x
		if v in marked:
			continue
		if len(path) > len(longestP):
			longestP = path
		elif len(path) == len(longestP):
			if path > longestP:
				longestP = path
		marked.add(v)
		for i,u in enumerate(edgeL[v]):
			p = path.copy()
			if u == 1:
				p.append(i)
				frontier.append((i,p))
	return(longestP)

#main
if __name__ == '__main__':
	wordL = [line.rstrip() for line in sys.stdin.readlines()]
	wordL.sort()
	edgeL = buildedgeL(wordL)
	longestP = []
	for v in range(len(wordL)):
		path = bfs(edgeL,v)
		if len(path) > len(longestP):
			longestP = path
	print(len(longestP))
	for i in longestP:
		print(wordL[i])
