# PROBLEM: Calculate in-degree minus out-degree for each vertex in directed graph
# INPUT: Multiple test cases, each with vertices, edges, and two arrays (starts, ends)
# OUTPUT: Space-separated list of (in-degree - out-degree) for each vertex
# KEYWORDS: directed graph, degree difference, in-degree, out-degree, flow balance

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases
t_var = int(input())

# process each test case
while t_var > 0:

    vertices_var, edges_var = map(int, input().split())  # node/edge counts
    
    start_var = list(map(int, input().split()))  # edge starts (1-based)
    
    end_var = list(map(int, input().split()))  # edge ends (1-based)
    
    diff_var = [0 for _ in range(vertices_var)]  # net flow per vertex
    
    i_var = 0  # edge cursor
    
    while i_var < edges_var:  # accumulate in/out degree difference
        
        diff_var[start_var[i_var] - 1] -= 1  # outgoing edge subtracts one
    
        diff_var[end_var[i_var] - 1] += 1  # incoming edge adds one
        
        i_var = i_var + 1
    
    print(*diff_var)  # output net differences space-separated
    
    # move to next test case
    t_var = t_var - 1
