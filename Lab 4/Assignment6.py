import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

size_var = int(input())  # board size (assumes 1..size_var coordinates)

position_var = list(map(int, input().split()))  # current cell [row, col]

moves_var = [  # all 8 king moves around the cell
    [position_var[0]-1, position_var[1]-1],
    [position_var[0]-1, position_var[1]],
    [position_var[0]-1, position_var[1]+1],
    [position_var[0], position_var[1]-1],
    [position_var[0], position_var[1]+1],
    [position_var[0]+1, position_var[1]-1],
    [position_var[0]+1, position_var[1]],
    [position_var[0]+1, position_var[1]+1]
]

store_var = []  # valid moves inside board

i_var = 0

while i_var < len(moves_var):  # filter in-bounds moves

    a_var, b_var = moves_var[i_var]  # candidate cell

    if a_var > 0 and a_var <= size_var and b_var > 0 and b_var <= size_var:
        
        store_var.append([a_var, b_var])  # keep valid move
        
    i_var = i_var + 1

print(len(store_var))  # count of legal moves

i_var = 0

while i_var < len(store_var):  # list each move

    print(*store_var[i_var])  # row col
    
    i_var = i_var + 1