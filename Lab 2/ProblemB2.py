import sys
d = sys.stdin.read().strip().split()
n = int(d[0])
m = int(d[1])
k = int(d[2])
i = 3 
a = []
b = []
c = 0 

while c < n:
    a.append(int(d[i]))
    c += 1
    i += 1

c = 0
while c< m:
    b.append(int(d[i]))
    c += 1
    i += 1

l = 0 
r = m - 1
b_l = 0
b_r = 0
b_d = float('inf')

while l < n and r >=0:
    sum = a[l] + b[r]
    diff = abs(sum - k)

    if diff < b_d:
        b_d = diff
        b_l = l 
        b_r = r

    if sum < k:
        l += 1
    else:
        r -= 1

sys.stdout.write(str(b_l + 1) + " "+ str(b_r + 1) + "\n")