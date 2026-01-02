import sys
input = sys.stdin.readline

N = int(input())
tasks = []

for _ in range(N):
    s,e = map(int, input().split())
    tasks.append((e,s))

tasks.sort()

res = []
last = -10**18

for e,s in tasks:
    if s > last:
        res.append((s,e))
        last = e

print(len(res))
for s,e in res:
    print(s,e)
