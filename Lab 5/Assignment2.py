import sys
from bisect import insort

input = sys.stdin.readline


vertices_var , edges_var = map(int , input().split())

inbound_var = list(map(int , input().split()))
outbound_var = list(map(int , input().split()))

adList_var = []
i_var = 0
while i_var < vertices_var:
    
    adList_var.append([])
    i_var = i_var + 1


k_var = 0
while k_var < edges_var:
    
    u_var = inbound_var[k_var]
    v_var = outbound_var[k_var]
    
    insort(adList_var[u_var - 1] , v_var)
    insort(adList_var[v_var - 1] , u_var)
    
    k_var = k_var + 1


visited_var = []
j_var = 0
while j_var < vertices_var:
    
    visited_var.append(0)
    j_var = j_var + 1


stack_var = [1]
dfs_var = []

while len(stack_var) > 0:
    
    node_var = stack_var.pop()
    
    if visited_var[node_var - 1] == 0:
        
        visited_var[node_var - 1] = 1
        dfs_var.append(node_var)
        
        p_var = len(adList_var[node_var - 1]) - 1
        
        while p_var >= 0:
            
            next_var = adList_var[node_var - 1][p_var]
            
            if visited_var[next_var - 1] == 0:
                stack_var.append(next_var)
            
            p_var = p_var - 1


print(*dfs_var)
