import sys
input = sys.stdin.readline

def find(a):
    while p[a] != a:
        p[a] = p[p[a]]
        a = p[a]
    return a

N, M = map(int, input().split())
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

p = list(range(N+1))
rank = [0]*(N+1)

ans = 0

for w, u, v in edges:
    pu = find(u)
    pv = find(v)
    if pu != pv:
        ans += w
        if rank[pu] < rank[pv]:
            pu, pv = pv, pu
        p[pv] = pu
        if rank[pu] == rank[pv]:
            rank[pu] += 1

print(ans)
