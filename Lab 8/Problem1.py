import sys
input = sys.stdin.readline

N, K = map(int, input().split())
parent = list(range(N+1))
sz = [1]*(N+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

out = []

for _ in range(K):
    a, b = map(int, input().split())
    pa = find(a)
    pb = find(b)

    if pa != pb:
        if sz[pa] < sz[pb]:
            pa, pb = pb, pa
        parent[pb] = pa
        sz[pa] += sz[pb]

    out.append(str(sz[find(a)]))

sys.stdout.write("\n".join(out))
