import sys

d = sys.stdin.read().strip().split()

n = int(d[0])

i = 1

while i <= n: 

    m = int(d[i])

    if m % 2 == 0:

        sys.stdout.write(str(m) + "This is an Even number. \n")
    else:
        sys.stdout.write(str(m) + "This is an Odd number. \n" )
    
    i = i + 1