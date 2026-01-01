import sys

from collections import deque

input = sys.stdin.readline

rows_var, cols_var = map(int, input().split())

grid_var = []

i_var = 0


while i_var < rows_var:

    grid_var.append(list(input().strip()))

    i_var = i_var + 1

visited_var = [[False for _ in range(cols_var)] for _ in range(rows_var)]

directions_var = [(1,0),(0,1),(-1,0),(0,-1)]

max_diamonds_var = 0

i_var = 0

while i_var < rows_var:

    j_var = 0

    while j_var < cols_var:

        if grid_var[i_var][j_var] != "#" and not visited_var[i_var][j_var]:

            queue_var = deque()

            queue_var.append((i_var,j_var))

            visited_var[i_var][j_var] = True

            diamonds_var = 0
            while queue_var:

                x_var, y_var = queue_var.popleft()
                if grid_var[x_var][y_var] == "D":
                    diamonds_var = diamonds_var + 1

                k_var = 0
                while k_var < 4:

                    new_x_var, new_y_var = x_var + directions_var[k_var][0], y_var + directions_var[k_var][1]
                    if 0 <= new_x_var < rows_var and 0 <= new_y_var < cols_var and not visited_var[new_x_var][new_y_var] and grid_var[new_x_var][new_y_var] != "#":
                        visited_var[new_x_var][new_y_var] = True

                        queue_var.append((new_x_var,new_y_var))

                    k_var = k_var + 1

            if diamonds_var > max_diamonds_var:

                max_diamonds_var = diamonds_var
        j_var = j_var + 1

    i_var = i_var + 1

print(max_diamonds_var)