#!/usr/bin/env python3
# Luke Song (csong1), Andy Shin (sshin1)
# challenge IIA

import sys, collections

# Construct adj list from the input
def create_graph(n):
    e = int(input().strip())
    graph = collections.defaultdict(list)
    for i in range(int(n)):
        graph[i] = []
    for _ in range(e):
        src, tgt = map(int, input().strip().split())
        graph[src-1].append(tgt-1)
        graph[tgt-1].append(src-1)
    return graph

# Main function to find groups in the graph
def find_groups(graph):
    groups = []
    for node in graph:
        visited = {node: False for node in graph}           # This gets updated during dfs call
        dfs(graph, visited, node)
        group = construct_group(visited)
        if group not in groups:
            groups.append(group)
    return groups

# construct group from the visited dict
def construct_group(visited):
    group = []
    for index, visited in visited.items():
        if visited == True:
            group.append(index+1)
    return ' '.join(map(str, sorted(group)))

# dfs to update visited
def dfs(graph, visited, v):
    if visited[v]:
        return
    visited[v] = True
    for neighbhor in graph[v]:
        if visited[neighbhor] == False:
            dfs(graph, visited, neighbhor)

if __name__ == '__main__':
    counter = 1
    while True:
        try:
            n = input().strip()
            graph = create_graph(n)
            groups = find_groups(graph)
            if len(groups) > 1:
                print("Graph {} has {} groups:".format(counter, len(groups)))
            else:
                print("Graph {} has {} group:".format(counter, len(groups)))
            for group in groups:
                print(group)
            counter += 1
        except EOFError:
            exit()

