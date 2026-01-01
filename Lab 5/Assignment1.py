import sys

from collections import deque

from bisect import insort

input = sys.stdin.readline

vertices_var , edges_var = map(int , input().split())

adjList_var = []

i_var = 0

while i_var < vertices_var:
    
    adjList_var.append([])
    
    i_var = i_var + 1

k_var = 0
while k_var < edges_var:
    
    u_var , v_var = map(int , input().split())
    
    insort(adjList_var[u_var - 1] , v_var)
    
    insort(adjList_var[v_var - 1] , u_var)
    
    k_var = k_var + 1

visited_var = []
j_var = 0

while j_var < vertices_var:
    
    visited_var.append(0)
    
    j_var = j_var + 1


queue_var = deque()
BFSorder_var = []

queue_var.append(0)
visited_var[0] = 1


while len(queue_var) > 0:
    
    u_var = queue_var.popleft()
    
    each_var = 0
    while each_var < len(adjList_var[u_var]):
        
        node_var = adjList_var[u_var][each_var]
        
        if visited_var[node_var - 1] != 1:
            
            queue_var.append(node_var - 1)
            
            visited_var[node_var - 1] = 1
        
        each_var = each_var + 1
    
    BFSorder_var.append(u_var + 1)

print(*BFSorder_var)
