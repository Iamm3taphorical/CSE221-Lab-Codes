import sys
d = sys.stdin.read().strip().split()
n = int(d[0])
x = int(d[1])

a = []
i = 2 
c = 0 
while c < n:
    value = int(d[i])
    a.append((value, c+1))
    c += 1
    i += 1
a.sort()
flag = False
i = 0 

while i < n - 2:
    first = a[i][0]
    left = 0
    right = n - 1
    target = x - first

    while left < right: 
        sum = a[left][0] + a[right][0]

        if sum == target: 
            sys.stdout.write(str(a[i][1] + a[left][1] + a[right[1] + "\n"]))
            flag = True
            break

        elif sum > target: 

            right -= 1

        else:
            left += 1
        
    if flag:
        break

    i += 1

if not flag:
    sys.stdout.write("-1\n")