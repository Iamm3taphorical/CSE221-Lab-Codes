import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
q = int(data[1])

a = []
i = 2
c = 0

while c < n:
    a.append(int(data[i]))
    i += 1
    c += 1

out = []
qc = 0

while qc < q:
    x = int(data[i])
    y = int(data[i + 1])
    i += 2

    l = 0
    r = n
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    lb = l

    l = 0
    r = n
    while l < r:
        m = (l + r) // 2
        if a[m] <= y:
            l = m + 1
        else:
            r = m
    ub = l

    res = ub - lb
    out.append(str(res) + "\n")

    qc += 1

sys.stdout.write("".join(out))