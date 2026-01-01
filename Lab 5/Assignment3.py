import sys
from collections import deque

def bfs_func(start_var, adjacency_list_var, vertices_var):
    
    distance_var = [-1] * (vertices_var + 1)
    distance_var[start_var] = 0
    
    queue_var = deque()
    queue_var.append(start_var)
    
    while queue_var:
        
        u_var = queue_var.popleft()
        neigh_var = adjacency_list_var[u_var]
        
        j_var = 0
        while j_var < len(neigh_var):
            v_var = neigh_var[j_var]
            
            if distance_var[v_var] == -1:
                distance_var[v_var] = distance_var[u_var] + 1
                queue_var.append(v_var)
            
            j_var = j_var + 1
    
    return distance_var



input = sys.stdin.readline

temp_var = list(map(int, input().split()))

vertices_var = temp_var[0]

edges_var = temp_var[1]

source_var = temp_var[2]

destination_var = temp_var[3]


inbound_var = list(map(int, input().split()))

outbound_var = list(map(int, input().split()))


adjacency_list_var = [[] for i in range(vertices_var + 1)]


i_var = 0

while i_var < edges_var:
    
    u_var = inbound_var[i_var]

    v_var = outbound_var[i_var]
    
    adjacency_list_var[u_var].append(v_var)

    adjacency_list_var[v_var].append(u_var)
    
    i_var = i_var + 1


i_var = 0

while i_var <= vertices_var:

    adjacency_list_var[i_var].sort()

    i_var = i_var + 1

distS_var = bfs_func(source_var, adjacency_list_var, vertices_var)

if distS_var[destination_var] == -1:

    print(-1)

else:
    
    distD_var = bfs_func(destination_var, adjacency_list_var, vertices_var)
    
    path_var = [source_var]

    cur_var = source_var

    total_steps_var = distS_var[destination_var]
    
    step_var = 0

    while step_var < total_steps_var:
        
        neigh_var = adjacency_list_var[cur_var]
        
        best_next_var = None
        
        j_var = 0

        while j_var < len(neigh_var):
            
            nxt_var = neigh_var[j_var]
            
            if distS_var[nxt_var] == distS_var[cur_var] + 1:

                if distS_var[nxt_var] + distD_var[nxt_var] == total_steps_var:
                    
                    best_next_var = nxt_var

                    break
            
            j_var = j_var + 1
        
        cur_var = best_next_var

        path_var.append(cur_var)
        
        step_var = step_var + 1
    
    
    print(total_steps_var)

    print(*path_var)