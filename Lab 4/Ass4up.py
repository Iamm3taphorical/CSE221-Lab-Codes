# PROBLEM: Determine if an Eulerian path or circuit exists in undirected graph
# INPUT: Multiple test cases, each with vertices, edges, and two arrays (starts, ends)
# OUTPUT: "YES" if graph has Eulerian path/circuit (0 or 2 odd-degree vertices), "NO" otherwise
# KEYWORDS: Euler path, Euler circuit, graph theory, degree counting, undirected graph

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases
t_var = int(input())

# process each test case
while t_var > 0:

    temp_var = input().split()  # first line tokens
    
    vertices_var = int(temp_var[0])  # number of vertices
    
    edges_var = int(temp_var[1])  # number of edges
    
    
    start_var = list(map(int, input().split()))  # edge starts (1-based)
    end_var = list(map(int, input().split()))  # edge ends (1-based)
    
    
    degree_var = [0] * vertices_var  # degree counts per vertex (0-based indexing)
    
    
    i_var = 0
    while i_var < edges_var:  # accumulate degrees
        
        u_var = start_var[i_var] - 1  # convert to 0-based
        v_var = end_var[i_var] - 1
        
        degree_var[u_var] += 1  # out/in both count for undirected degree
    
        degree_var[v_var] += 1
        
        i_var = i_var + 1
    
    
    odd_var = 0  # count of odd-degree vertices
    i_var = 0
    
    while i_var < vertices_var:
        
        if degree_var[i_var] % 2 != 0:  # odd degree check
    
            odd_var = odd_var + 1
        
        i_var = i_var + 1
    
    
    if odd_var == 0 or odd_var == 2:  # Euler circuit/path condition
    
        print("YES")
    else:
        print("NO")
    
    # move to next test case
    t_var = t_var - 1
