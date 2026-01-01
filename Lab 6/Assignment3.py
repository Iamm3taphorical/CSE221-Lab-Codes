import sys
# fast input for large chessboard sizes
input = sys.stdin.readline

# read board size `n`
# read starting position (a, b)
# read target position (c, d)
n = int(input())
a, b, c, d = map(int, input().split())

# visited 2D array `v` (1-indexed)
# v[x][y] = 1 means the cell (x,y) has already been visited
v = [[0] * (n + 1) for _ in range(n + 1)]

# distance 2D array `D` to store the number of knight moves
# D[x][y] = minimum knight moves required to reach (x,y) from (a,b)
D = [[0] * (n + 1) for _ in range(n + 1)]

# knight movement offsets:
# a knight moves in (±2, ±1) or (±1, ±2) patterns
mx = [2, 2, -2, -2, 1, 1, -1, -1]
my = [1, -1, 1, -1, 2, -2, 2, -2]

# arrays for BFS queue storing coordinates separately
# qx[] stores x-coordinates in queue
# qy[] stores y-coordinates in queue
qx = [0] * ((n * n) + 5)
qy = [0] * ((n * n) + 5)

# front and back pointers for queue
f = 0      # index of current element being popped
bk = 0     # index where new elements are pushed

# enqueue the starting position into the BFS queue
qx[bk] = a
qy[bk] = b
bk = bk + 1

# mark starting cell (a,b) visited
v[a][b] = 1

# F = 1 means target was found; 0 means not found
F = 0

# BFS loop — continues until queue becomes empty
while f < bk:
    cx = qx[f]   # current x coordinate from queue
    cy = qy[f]   # current y coordinate from queue
    f = f + 1    # pop from queue

    # check if current cell is the target (c, d)
    if cx == c and cy == d:
        print(D[cx][cy])   # print number of moves needed
        F = 1              # mark that we found target
        break              # stop BFS

    # try all 8 possible knight moves
    i = 0
    while i < 8:
        nx = cx + mx[i]     # calculate new x-position
        ny = cy + my[i]     # calculate new y-position

        # check if new position is within board limits
        if 1 <= nx <= n and 1 <= ny <= n:
            # check if this cell has not been visited before
            if v[nx][ny] == 0:
                v[nx][ny] = 1                   # mark as visited
                D[nx][ny] = D[cx][cy] + 1       # update distance
                qx[bk] = nx                     # push new x
                qy[bk] = ny                     # push new y
                bk = bk + 1                     # queue grows
        i = i + 1

# if BFS completed and target was never reached
if F == 0:
    print(-1)