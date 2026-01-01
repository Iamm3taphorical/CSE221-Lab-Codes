import sys  # fast stdin/stdout
input = sys.stdin.readline  # quicker line reads

N_var, M_var = map(int, input().split())  # number of nodes and edges

adjList_var = [[] for i in range(N_var + 1)]  # 1-based adjacency list

i_var = 0  # edge counter
while i_var < M_var:  # read all edges

    u_var, v_var = map(int, input().split())  # endpoints (1-based)

    adjList_var[u_var].append(v_var)  # add neighbor to u

    adjList_var[v_var].append(u_var)  # add neighbor to v (undirected)
    i_var = i_var + 1   

visited_var = [0] * (N_var + 1)  # visited marker per node
bfsOrder_var = []  # traversal order output

queue_var = [0] * (N_var + 5)  # fixed-size queue buffer
front_var = 0  # dequeue index
back_var = 0  # enqueue index (exclusive)

visited_var[1] = 1  # start BFS at node 1
queue_var[back_var] = 1  # enqueue start
back_var = back_var + 1 

while front_var < back_var:  # process until queue empty

    u_var = queue_var[front_var]  # pop front node

    front_var = front_var + 1  # advance front pointer

    bfsOrder_var.append(u_var)  # record visitation

    for v_var in adjList_var[u_var]:  # explore neighbors

        if visited_var[v_var] == 0:  # unvisited neighbor

            visited_var[v_var] = 1  # mark visited

            queue_var[back_var] = v_var  # enqueue neighbor
            back_var = back_var + 1 

print(*bfsOrder_var)  # output BFS order space-separated