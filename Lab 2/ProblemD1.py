import sys 

d = sys.stdin.read().strip().split()
result = []
n = int(d[0])
c = 0
a = []
b = []

i = 1
while c < n:
    a.append(int(d[i]))
    i += 1
    c += 1

m = int(d[i])
i += 1
c = 0

while c < m:
    b.append(int(d[i]))
    i += 1
    c += 1

l = 0
r = 0 

while l < n and r < m:

    if a[l] <= b[r]:
        result.append(a[l])
        l += 1
    
    else: 
        result.append(b[r])
        r += 1

while l < n: 
    result.append(a[l])
    l += 1

while r < m:
    result.append(b[r])
    r += 1

i = 0
while i < len(result):
    sys.stdout.write(str(result[i]) + " ")
    i += 1
sys.stdout.write("\n")