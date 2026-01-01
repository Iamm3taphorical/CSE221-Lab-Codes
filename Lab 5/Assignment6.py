import sys

from collections import deque

input = sys.stdin.readline

vertices_var, edges_var = map(int, input().split())

adjacency_list_var = [[] for _ in range(vertices_var + 1)]

i_var = 0

while i_var < edges_var:

    u_var, v_var = map(int, input().split())

    adjacency_list_var[u_var].append(v_var)

    i_var = i_var + 1

visited_var = [0 for _ in range(vertices_var + 1)]

rec_stack_var = [0 for _ in range(vertices_var + 1)]

answer_var = False

i_var = 1

while i_var <= vertices_var:

    if visited_var[i_var] == 0:

        stack_var = [(i_var, 0)]

        while stack_var:

            u_var, idx_var = stack_var[-1]

            if visited_var[u_var] == 0:

                visited_var[u_var] = 1

                rec_stack_var[u_var] = 1

            neighbors_var = adjacency_list_var[u_var]

            if idx_var < len(neighbors_var):

                v_var = neighbors_var[idx_var]

                stack_var[-1] = (u_var, idx_var + 1)

                if visited_var[v_var] == 0:
                    stack_var.append((v_var, 0))

                elif rec_stack_var[v_var] == 1:

                    answer_var = True

                    stack_var.clear()

                    break
            else:
                rec_stack_var[u_var] = 0

                stack_var.pop()

    if answer_var:
        
        break

    i_var = i_var + 1

if answer_var:

    print("YES")

else:

    print("NO")