import sys
# fast input for large testcases
input = sys.stdin.readline

# read number of nodes `n` and edges `m`
n, m = map(int, input().split())

# adjacency list `g` for undirected graph; 1-indexed
g = [[] for i in range(n + 1)]

# read edges and fill adjacency list
i = 0
while i < m:
    u, v = map(int, input().split())  # endpoints of undirected edge
    g[u].append(v)                     # add v to u's neighbours
    g[v].append(u)                     # add u to v's neighbours
    i = i + 1                           # processed one edge

# color array: 0 = unvisited, 1 and 2 are the two colors
c = [0] * (n + 1)

# queue implemented as fixed-size list for BFS
q = [0] * (n + 5)

# answer accumulator
ans = 0

# iterate through each node to start BFS on unvisited components
u = 1
while u <= n:
    if c[u] == 0:               # component not yet visited
        f = 0                   # queue front index
        b = 0                   # queue back index
        q[b] = u               # enqueue starting node
        b = b + 1
        c[u] = 1               # assign color 1 to start node

        # counters for nodes of each color inside this component
        x = 0
        y = 0

        # BFS loop over component
        while f < b:
            cur = q[f]         # current node from queue
            f = f + 1

            # count per-color nodes
            if c[cur] == 1:
                x = x + 1
            else:
                y = y + 1

            idx = 0
            nbrs = g[cur]      # neighbours of current node
            # iterate adjacency list by index (keeps original style)
            while idx < len(nbrs):
                w = nbrs[idx]
                if c[w] == 0:    # unvisited neighbour
                    # assign opposite color to maintain bipartiteness
                    if c[cur] == 1:
                        c[w] = 2
                    else:
                        c[w] = 1
                    q[b] = w      # enqueue neighbour
                    b = b + 1
                idx = idx + 1

        # add the larger color group of the component to answer
        if x > y:
            ans = ans + x
        else:
            ans = ans + y
    u = u + 1

# output final result
print(ans)