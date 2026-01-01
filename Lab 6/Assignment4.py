import sys
# fast input
input = sys.stdin.readline

# read number of nodes `n` in the tree
n = int(input())

# adjacency list `g` for the tree (1-indexed)
# g[i] will store all neighbors of node i
g = [[] for i in range(n + 1)]

# read the n-1 edges of the tree and build adjacency list
i = 0
while i < n - 1:
    u, v = map(int, input().split())   # read endpoints of an edge
    g[u].append(v)                     # add v to u’s adjacency list
    g[v].append(u)                     # add u to v’s adjacency list
    i = i + 1

def bfs(s):
    # vis[i] = 1 means node i is visited, 0 means not visited
    vis = [0] * (n + 1)

    # D[i] stores the distance from source `s` to node i
    D = [0] * (n + 1)

    # queue for BFS, implemented manually for speed
    q = [0] * (n + 5)
    f = 0             # front pointer
    b = 0             # back pointer

    q[b] = s          # push source node s
    b = b + 1
    vis[s] = 1        # mark source as visited

    last = s          # will store last popped node (farthest found)

    # standard BFS loop
    while f < b:
        x = q[f]      # get current node from queue
        f = f + 1
        last = x      # update last visited node

        idx = 0
        nbrs = g[x]   # list of neighbors of x

        # iterate over all neighbors
        while idx < len(nbrs):
            y = nbrs[idx]
            # if neighbor y is not visited
            if vis[y] == 0:
                vis[y] = 1
                D[y] = D[x] + 1    # distance = parent's distance + 1
                q[b] = y           # enqueue y
                b = b + 1
            idx = idx + 1

    # return:
    # last  = farthest node from s
    # D[last] = its distance from s
    # D = full distance array
    return last, D[last], D

# run BFS from node 1 to find one endpoint A of the tree diameter
A, _, _ = bfs(1)

# run BFS from A; this finds the opposite endpoint B and the diameter length
B, diam, _ = bfs(A)

# output the diameter length
print(diam)
# output the two endpoints of the diameter
print(A, B)