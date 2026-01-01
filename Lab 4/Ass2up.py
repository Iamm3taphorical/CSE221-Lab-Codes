# PROBLEM: Build and print weighted adjacency list for directed graphs
# INPUT: Multiple test cases, each with vertices, edges, and three arrays (starts, ends, weights)
# OUTPUT: For each vertex, print "vertex: (neighbor, weight) (neighbor, weight) ..."
# KEYWORDS: adjacency list, directed graph, weighted edges, graph representation

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases from first line
t_var = int(input())

# process each test case
while t_var > 0:

    vertices_var , edges_var = map(int , input().split())  # counts of nodes and edges
    
    adjList_var = []  # adjacency list (1-based in input, stored 0-based rows)
    
    i_var = 0  # vertex index
    
    while i_var < vertices_var:  # initialize empty lists for each vertex
        
        adjList_var.append([])  # row for outgoing edges
        
        i_var = i_var + 1
    
    start_var = list(map(int , input().split()))  # edge start nodes (1-based)
    
    end_var   = list(map(int , input().split()))  # edge end nodes (1-based)
    
    weight_var = list(map(int , input().split()))  # edge weights aligned by index
    
    
    k_var = 0  # edge cursor
    
    while k_var < edges_var:  # build adjacency list
        
        node_u_var = start_var[k_var] - 1  # convert start to 0-based row
    
        node_v_var = end_var[k_var]  # keep destination 1-based as stored
    
        cost_var   = weight_var[k_var]  # weight of this edge
        
        adjList_var[node_u_var].append((node_v_var , cost_var))  # append tuple(dest, weight)
        
        k_var = k_var + 1
    
    x_var = 0  # print cursor
    
    while x_var < vertices_var:  # output adjacency list
        
        print(str(x_var + 1) + ":", *adjList_var[x_var])  # prefix with node label (1-based)
        
        x_var = x_var + 1
    
    # move to next test case
    t_var = t_var - 1