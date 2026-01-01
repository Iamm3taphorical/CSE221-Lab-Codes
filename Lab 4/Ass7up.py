# PROBLEM: Detect if any two knights on a chessboard can attack each other
# INPUT: Multiple test cases, each with board dimensions, knight count, and knight positions
# OUTPUT: "YES" if any knight attacks another, "NO" if all knights are safe
# KEYWORDS: chess knight moves, L-shaped movement, conflict detection, attack validation

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

# read number of test cases from first line
t_var = int(input())

# process each test case
while t_var > 0:

    rows_var, columns_var, knights_var = map(int, input().split())  # board size and knight count
    
    positions_var = {}  # map of occupied cells -> index (used as presence set)
    
    
    i_var = 0  # knight counter
    
    while i_var < knights_var:  # read knight positions
    
        pos_var = tuple(map(int, input().split()))  # (row, col) as tuple for hashing
    
        positions_var[pos_var] = i_var  # store occupancy in dictionary
    
        i_var = i_var + 1
    
    flag_var = True  # assume no attacks initially (innocent until proven guilty)
    
    for pos_var in positions_var.keys():  # check each knight's position
    
        moves_var = [  # all 8 possible knight moves from current position
            (pos_var[0] - 2, pos_var[1] - 1),  # 2 up, 1 left
            (pos_var[0] - 2, pos_var[1] + 1),  # 2 up, 1 right
            (pos_var[0] - 1, pos_var[1] - 2),  # 1 up, 2 left
            (pos_var[0] - 1, pos_var[1] + 2),  # 1 up, 2 right
            (pos_var[0] + 1, pos_var[1] - 2),  # 1 down, 2 left
            (pos_var[0] + 1, pos_var[1] + 2),  # 1 down, 2 right
            (pos_var[0] + 2, pos_var[1] - 1),  # 2 down, 1 left
            (pos_var[0] + 2, pos_var[1] + 1)   # 2 down, 1 right
        ]
    
        j_var = 0  # move index
    
        while j_var < len(moves_var):  # test each reachable square
    
            if moves_var[j_var] in positions_var:  # another knight found at this position
    
                flag_var = False  # attack detected
    
                break  # no need to check more moves for this knight
    
            j_var = j_var + 1
        
        if not flag_var:  # early exit if any attack detected
    
            break  # stop checking other knights
    
    if flag_var:  # no attacks found across all knights
    
        print("NO")  # output NO (no attacks)
    else:
        
        print("YES")  # output YES (attacks exist)
    
    # move to next test case
    t_var = t_var - 1
