#!/usr/bin/env python3
# Sung Hyun Shin (sshin1) & Luke Song (csong1)

import sys, collections, math

# Create 2d matrix from input
def create_matrix(m, n):
    matrix = []
    if n == 1:
        for i in range(m):
            matrix.append(int(input().strip()))
    else:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            matrix[i] = list(map(int, input().strip().split()))
    return matrix

# Make adj_list from matrix, transform row, col to cell ID to easier path calculation
def make_graph(matrix, row, col, matrix_map):
    adj_list = collections.defaultdict(set)
    for i in range(row * col):
        adj_list[i] = set()
    counter = 0                                                     # Counter for cell ID
    for i in range(row):
        for j in range(col):
            matrix_map[counter] = (i+1, j+1)
            ## Check cells around
            # check top row
            if j+1 >= col:                                          # If top right column, just skip
                counter += 1
                continue
            if i-1 >= 0:
                adj_list[counter].add((counter-col+1, matrix[i-1][j+1]))
            else:
                adj_list[counter].add((counter+(row-1)*col+1, matrix[row-1][j+1]))
            # check middle row
            adj_list[counter].add((counter+1, matrix[i][j+1]))
            # check bottom row
            if i+1 < row:
                adj_list[counter].add((counter+col+1, matrix[i+1][j+1]))
            else:
                adj_list[counter].add((counter-(row-1)*col+1, matrix[0][j+1])) 
            counter += 1
    return adj_list

# Bellman Ford algorithm to get min weight path
def BellmanFord(graph, row, col, source):
    weight = [math.inf for _ in range(row * col)]
    previous = [math.inf for _ in range(row * col)]
    weight[source] = 0
    for i in range(0, row*col):
        for v in graph:
            for tgt, w in graph[v]:
                curr_dist = weight[v] + w
                if curr_dist < weight[tgt]:
                    weight[tgt] = weight[v] + w
                    previous[tgt] = v
                elif curr_dist == weight[tgt]:                    # Extra check to insure top right one is selected in case of same weight     
                    if v < previous[tgt]:
                        previous[tgt] = v
    return previous, weight 

# Utility function to construct path from previous and weight list
def construct_path(matrix_map, matrix, previous, weight, start, end):
    start_weight = matrix[matrix_map[start][0]-1][0]                  # Get start cell weight from matrix and matrix_map
    total_weight = weight[end] + start_weight
    curr = previous[end]
    path = [curr, end]
    while curr != start:
        curr = previous[curr]
        path.insert(0, curr)
    return path, total_weight

# Utility function to change path format back to row, col
def change_path_format(path, matrix_map):
    final_path = []
    for cell_id in path:
        final_path.append(matrix_map[cell_id][0])
    return ' '.join(map(str, final_path))

# Utility function to find start and end points in the matrix, transform to cell ID
def start_end(m, n):
    start = []
    end = []
    for i in range(m):
        start.append(0 + i*n)
        end.append(n-1 + i*n)
    return start, end

# Main
if __name__ == '__main__':
    while True:
        try:
            m, n = map(int, input().strip().split())
            matrix = create_matrix(m, n)
            # Some edge cases where (m or n is 0) or n = 1
            if m == 0 or n == 0:
                continue
            if n == 1:
                min_cost = min(matrix)
                print(min_cost)
                print(matrix.index(min_cost)+1)
                continue
            matrix_map = collections.defaultdict(tuple)
            graph = make_graph(matrix, m, n, matrix_map)
            start, end = start_end(m, n)
            min_dist = math.inf
            min_path = []
            # Iterate through start and end pairs and construct path
            for cell_s in start:
                previous, weight = BellmanFord(graph, m, n, cell_s)               # Bellman Ford calculates weight to every node reachable
                for cell_e in end:
                    if weight[cell_e] != math.inf:                                # only construct path when end cell is reachable
                        path, total_weight = construct_path(matrix_map, matrix, previous, weight, cell_s, cell_e)   
                        if total_weight < min_dist:
                            min_path = path
                            min_dist = total_weight
            final_path = change_path_format(min_path, matrix_map)
            print(min_dist)
            print(final_path)
        except EOFError:
            exit()    
