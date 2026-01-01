import sys
# use fast input because constraints may be large
input = sys.stdin.readline

# read number of nodes n, edges m, number of sources s, number of queries q
n, m, s, q = map(int, input().split())

# create adjacency list g for an undirected graph of size n
g = [[] for i in range(n + 1)]

# read all m undirected edges
i = 0
while i < m:
    u, v = map(int, input().split())   # endpoints of edge
    g[u].append(v)                     # add v to u’s list
    g[v].append(u)                     # add u to v’s list
    i += 1

# read list of s source nodes
S = list(map(int, input().split()))
# read list of q destination nodes for queries
Dlist = list(map(int, input().split()))

# dist[i] will store distance of node i from nearest source
# -1 means node has not been visited yet / unreachable
dist = [-1] * (n + 1)

# queue array used to implement BFS without using collections.deque
qarr = [0] * (n + 5)
f = 0        # front pointer of queue
bk = 0       # back pointer of queue

# push all source nodes into queue with distance 0
i = 0
while i < s:
    x = S[i]          # current source node
    dist[x] = 0       # distance from source to itself is 0
    qarr[bk] = x      # enqueue node
    bk += 1
    i += 1

# perform multi-source BFS
# this computes minimum distance from ANY source for every node
while f < bk:
    u = qarr[f]       # dequeue next node
    f += 1
    # explore all neighbors of u
    for v in g[u]:
        # if neighbor v has not been visited yet
        if dist[v] == -1:
            dist[v] = dist[u] + 1   # update distance
            qarr[bk] = v            # enqueue neighbor
            bk += 1

# answer each query by retrieving precomputed distance
ans = []
i = 0
while i < q:
    d = Dlist[i]      # requested destination node
    ans.append(dist[d])
    i += 1

# output all answers in one line
print(*ans)