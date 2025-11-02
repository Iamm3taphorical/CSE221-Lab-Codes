import sys

data = sys.stdin.read().strip().split()

n = int(data[0])
k = int(data[1])

a = []
i = 2
c = 0

while c < n:
    a.append(int(data[i]))
    i = i + 1
    c = c + 1

l = 0
r = 0
mx = 0

f = [0] * (n + 1)
d = 0

while r < n:
    curr = a[r]
    if f[curr] == 0:
        d = d + 1
    f[curr] = f[curr] + 1

    while d > k:
        left = a[l]
        f[left] = f[left] - 1
        if f[left] == 0:
            d = d - 1
        l = l + 1

    win = r - l + 1
    if win > mx:
        mx = win

    r = r + 1

sys.stdout.write(str(mx) + "\n")