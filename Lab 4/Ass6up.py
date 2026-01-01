# PROBLEM: Find all valid king moves from a given position on a chessboard
# INPUT: Multiple test cases, each with board size and king position (row, col)
# OUTPUT: Count of valid moves, then each valid destination (row, col)
# KEYWORDS: chess king moves, grid movement, boundary checking, 8-directional movement

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases from first line
t_var = int(input())

# process each test case
while t_var > 0:

    size_var = int(input())  # board size (assumes 1..size_var coordinates)
    
    position_var = list(map(int, input().split()))  # current cell [row, col]
    
    moves_var = [  # all 8 king moves around the cell
        [position_var[0]-1, position_var[1]-1],  # up-left diagonal
        [position_var[0]-1, position_var[1]],    # directly up
        [position_var[0]-1, position_var[1]+1],  # up-right diagonal
        [position_var[0], position_var[1]-1],    # directly left
        [position_var[0], position_var[1]+1],    # directly right
        [position_var[0]+1, position_var[1]-1],  # down-left diagonal
        [position_var[0]+1, position_var[1]],    # directly down
        [position_var[0]+1, position_var[1]+1]   # down-right diagonal
    ]
    
    store_var = []  # valid moves inside board boundaries
    
    i_var = 0  # move index
    
    while i_var < len(moves_var):  # filter in-bounds moves
    
        a_var, b_var = moves_var[i_var]  # candidate cell coordinates
    
        if a_var > 0 and a_var <= size_var and b_var > 0 and b_var <= size_var:  # check boundaries
            
            store_var.append([a_var, b_var])  # keep valid move
            
        i_var = i_var + 1  # check next move
    
    print(len(store_var))  # output count of legal moves
    
    i_var = 0  # reset index for printing
    
    while i_var < len(store_var):  # list each valid move
    
        print(*store_var[i_var])  # print row col space-separated
        
        i_var = i_var + 1
    
    # move to next test case
    t_var = t_var - 1
