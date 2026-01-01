import sys

from collections import deque

input = sys.stdin.readline


def bfs(start_var, adj_var, n_var):
    
    queue_var = deque()

    queue_var.append(start_var)
    
    dist_var = [-1] * (n_var + 1)

    parent_var = [0] * (n_var + 1)
    
    dist_var[start_var] = 0
    
    while queue_var:
        
        u_var = queue_var.popleft()
        
        for v_var in adj_var[u_var]:
            
            if dist_var[v_var] == -1:
                
                dist_var[v_var] = dist_var[u_var] + 1

                parent_var[v_var] = u_var
                
                queue_var.append(v_var)
    
    return dist_var, parent_var



def path_finder(dest_var, src_var, parent_var):
    
    path_var = []

    cur_var = dest_var
    
    while cur_var != 0:
        
        path_var.append(cur_var)
        
        if cur_var == src_var:

            break
        
        cur_var = parent_var[cur_var]
    
    path_var.reverse()
    
    return path_var



temp_var = list(map(int, input().split()))

vertices_var = temp_var[0]

edges_var = temp_var[1]

source_var = temp_var[2]

dest_var = temp_var[3]

mandatory_var = temp_var[4]


adj_var = [[] for _ in range(vertices_var + 1)]


i_var = 0

while i_var < edges_var:
    
    u_var, v_var = map(int, input().split())

    adj_var[u_var].append(v_var)
    
    i_var = i_var + 1


distS_var, parentS_var = bfs(source_var, adj_var, vertices_var)

if distS_var[mandatory_var] == -1:

    
    print(-1)

else:
    
    distM_var, parentM_var = bfs(mandatory_var, adj_var, vertices_var)
    
    if distM_var[dest_var] == -1:
        
        print(-1)
    
    else:
        
        part1_var = path_finder(mandatory_var, source_var, parentS_var)

        part2_var = path_finder(dest_var, mandatory_var, parentM_var)
        
        final_path_var = part1_var + part2_var[1:]
        
        print(len(final_path_var) - 1)
        
        print(*final_path_var)