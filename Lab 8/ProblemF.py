import sys
input = sys.stdin.readline

n = int(input())
tasks = []

for _ in range(n):
    a,d = map(int, input().split())
    tasks.append((a,d))

tasks.sort()

t = 0
reward = 0

for a,d in tasks:
    t += a
    reward += d - t

print(reward)
