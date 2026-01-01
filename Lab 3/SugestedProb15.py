import sys
input = sys.stdin.readline

N, A, B, C = map(int, input().split())

prev = A*0*0 + B*0*0 + C*0*0
current = 1
ans = 1

for x in range(N):
    for y in range(N):
        val = A*x*x + B*y*y + C*x*y
        if x == 0 and y == 0:
            continue
        if val > prev:
            current += 1
        else:
            current = 1
        ans = max(ans, current)
        prev = val

print(ans)