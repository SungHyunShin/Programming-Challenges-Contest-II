#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys

# checks if two words are word morphs of each other
def isWordMorph(w1,w2):
	diff = 0
	# if w2 is 1 char longer
	if len(w1)+1 == len(w2):
		if w1[0] is not w2[0]:
			w2 = w2[1:]
			diff += 1
		elif w1[-1] is not w2[-1]:
			w2 = w2[:-1]
			diff += 1
	# else if w1 is 1 char longer
	elif len(w1) == len(w2)+1:
		if w1[0] is not w2[0]:
			w1 = w1[1:]
			diff += 1
		elif w1[-1] is not w2[-1]:
			w1 = w1[:-1]
			diff += 1
	# else if they're not the same length
	elif len(w1) is not len(w2):
		return False
	# if they're equal lengths or 1 char longer than each other
	if len(w1) == len(w2):
		for i in range(len(w1)):
			if w1[i] is not w2[i]:
				diff +=1
		# if there's one or less differences
		return diff <= 1
	# else return false
	else:
		return False

# edge list where if 1 can go to 2 or 3, edgeL[1] = [2,3]
def buildedgeL(wordL):
	edgeL = []
	for i in range(len(wordL)):
		edgeL.append([])
	for i in range(len(wordL)):
		for j in range(i+1, len(wordL)):
			if isWordMorph(wordL[j],wordL[i]):
				edgeL[i].append(j)
	return edgeL

# recursive depth first that returns a list of all paths
def dfs_rec(edgeL,v,marked,path,paths):
	if v in marked:
		return
	marked.add(v)
	paths.append(path)
	for i in edgeL[v]:
		p = path.copy()
		p.append(i)
		dfs_rec(edgeL,i,marked,p,paths)
	return paths

#main
if __name__ == '__main__':
	wordL = [line.rstrip() for line in sys.stdin.readlines()]
	wordL.sort()
	edgeL = buildedgeL(wordL)
	longestPath = []
	# run dfs for all nodes (bc they can be disconnected) and get longest path
	for edge in range(len(edgeL)):
		path = []
		path.append(edge)
		paths = dfs_rec(edgeL,edge,set(),path,[])
		longestPath = max(longestPath,max(paths,key=len),key=len)
	# print cost
	print(len(longestPath))
	# print words
	for i in longestPath:
		print(wordL[i])
