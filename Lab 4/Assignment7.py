import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

rows_var, columns_var, knights_var = map(int, input().split())  # board size and knight count

positions_var = {}  # map of occupied cells -> index (presence set)


i_var = 0  # knight counter

while i_var < knights_var:  # read knight positions

    pos_var = tuple(map(int, input().split()))  # (row, col)

    positions_var[pos_var] = i_var  # store occupancy

    i_var = i_var + 1

flag_var = True  # assume no attacks initially

for pos_var in positions_var.keys():  # check each knight

    moves_var = [  # all 8 knight moves from current square
        (pos_var[0] - 2, pos_var[1] - 1),
        (pos_var[0] - 2, pos_var[1] + 1),
        (pos_var[0] - 1, pos_var[1] - 2),
        (pos_var[0] - 1, pos_var[1] + 2),
        (pos_var[0] + 1, pos_var[1] - 2),
        (pos_var[0] + 1, pos_var[1] + 2),
        (pos_var[0] + 2, pos_var[1] - 1),
        (pos_var[0] + 2, pos_var[1] + 1)
    ]

    j_var = 0

    while j_var < len(moves_var):  # test each reachable square

        if moves_var[j_var] in positions_var:  # another knight found

            flag_var = False  # attack exists

            break

        j_var = j_var + 1
    if not flag_var:  # early exit if attack detected

        break

if flag_var:  # no attacks

    print("NO")
else:
    
    print("YES")