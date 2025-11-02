import sys

data = sys.stdin.read().strip().split()

t = int(data[0])
idx = 1

while t > 0:
    k = int(data[idx])
    x = int(data[idx + 1])
    idx += 2

    l = 1
    r = k * x

    while l < r:
        m = (l + r) // 2
        c = m - (m // x)

        if c < k:
            l = m + 1
        else:
            r = m

    sys.stdout.write(str(l) + "\n")

    t -= 1