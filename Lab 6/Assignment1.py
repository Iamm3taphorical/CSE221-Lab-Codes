import sys
# fast input reading
input = sys.stdin.readline

# read N (nodes) and M (edges)
N, M = map(int, input().split())

# adjacency list for directed graph
adj = [[] for _ in range(N + 1)]

# indegree array
ind = [0] * (N + 1)

# read M edges
i = 0
while i < M:
    A, B = map(int, input().split())  # edge A → B
    adj[A].append(B)                 # store directed edge
    ind[B] = ind[B] + 1              # increase indegree of B
    i = i + 1

# queue for nodes with indegree 0
q = [0] * (N + 5)
f = 0   # front pointer for queue
b = 0   # back pointer for queue

# push all nodes with indegree 0
i = 1
while i <= N:
    if ind[i] == 0:       # if node has no incoming edges
        q[b] = i          # push into queue
        b = b + 1
    i = i + 1

# list to store topological order
order = []

# BFS-like topological sorting
while f < b:
    u = q[f]              # pop from queue
    f = f + 1
    order.append(u)       # include in ordering

    j = 0
    # go through all outgoing edges u → v
    while j < len(adj[u]):
        v = adj[u][j]
        ind[v] = ind[v] - 1     # reduce indegree of v
        if ind[v] == 0:         # if v now has no incoming edges
            q[b] = v            # push into queue
            b = b + 1
        j = j + 1

# if ordering does not include all nodes → cycle exists
if len(order) != N:
    print(-1)
else:
    print(*order)