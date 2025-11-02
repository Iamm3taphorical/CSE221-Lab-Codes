import sys 
data_var = sys.stdin.read().strip().split()
n = int(data_var[0])
s = int(data_var[1])
arr = []
i = 2
while i < n + 2:
    arr.append(int(data_var[i]))
    i += 1
l = 0
r = n - 1
sum = 0
flag = False
while l < r:
    sum = arr[l] + arr[r]
    if sum == s:
        sys.stdout.write(str(l+1)+ " " + str(r+1)+ "\n")
        flag = True 
        break
    elif sum> s: 
        r = r -1
    else:
        l = l + 1
if not flag:
    sys.stdout.write("-1\n")            