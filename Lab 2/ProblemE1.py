import sys
d = sys.stdin.read().strip().split()
n = int(d[0])
k = int(d[1])
a = []
i = 2
c = 0 
while c < n:
    a.append(int(d[i]))
    i += 1
    c += 1
l = 0 
r = 0 
s = 0 
m = 0 
while r < n:
    s = s + a[r]
    while s > k and l <= r:
        s = s - a[l]
        l += 1
    len = r - l + 1
    if s <= k:
        if len > m:
            m = len
    r += 1
sys.stdout.write(str(m)+ "\n")