# PROBLEM: Convert adjacency list representation to adjacency matrix
# INPUT: Multiple test cases, each with N vertices and N lines of adjacency lists (count followed by neighbors)
# OUTPUT: N x N binary matrix where matrix[i][j] = 1 if edge exists from i to j, else 0
# KEYWORDS: adjacency list to matrix, graph conversion, unweighted graph, graph representation

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases from first line
t_var = int(input())

# process each test case
while t_var > 0:

    vertices_var = int(input())  # number of vertices (0..vertices_var-1)
    
    array_var = []  # adjacency matrix container
    
    i_var = 0  # row builder index
    
    while i_var < vertices_var:  # initialize zero matrix
        
        row_var = []  # row placeholder
    
        j_var = 0  # column index
        
        while j_var < vertices_var:
    
            row_var.append(0)  # no edges yet
    
            j_var = j_var + 1
        
        array_var.append(row_var)  # store completed row
    
        i_var = i_var + 1
    
    i_var = 0  # row index for input edges
    
    while i_var < vertices_var:  # read adjacency lists row by row
        
        store_var = list(map(int, input().split()))  # first token is count, rest are neighbors
        
        j_var = 1            
                    
        while j_var < len(store_var):  # iterate over neighbors
    
            col_var = store_var[j_var]  # neighbor vertex (0-based expected)
    
            array_var[i_var][col_var] = 1  # mark edge i_var -> col_var
            
            j_var = j_var + 1
    
        i_var = i_var + 1
    
    i_var = 0
    while i_var < vertices_var:  # output matrix rows
        
        print(*array_var[i_var])  # space-separated row
        
        i_var = i_var + 1
    
    # move to next test case
    t_var = t_var - 1