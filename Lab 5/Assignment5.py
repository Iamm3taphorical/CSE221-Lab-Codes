import sys
from collections import deque

input = sys.stdin.readline

nodes_var, root_var = map(int, input().split())

adj_list_var = [[] for _ in range(nodes_var+1)]

i_var = 1

while i_var < nodes_var:

    u_var, v_var = map(int, input().split())

    adj_list_var[u_var].append(v_var)
    
    adj_list_var[v_var].append(u_var)

    i_var = i_var + 1

parent_var = [0 for _ in range(nodes_var+1)]

queue_var = deque()

order_var = []

queue_var.append(root_var)

parent_var[root_var] = -1

while queue_var:

    u_var = queue_var.popleft()

    order_var.append(u_var)

    j_var = 0
    while j_var < len(adj_list_var[u_var]):

        v_var = adj_list_var[u_var][j_var]

        if v_var != parent_var[u_var]:
            
            parent_var[v_var] = u_var

            queue_var.append(v_var)

        j_var = j_var + 1

subtree_var = [0 for _ in range(nodes_var+1)]

order_var.reverse()

i_var = 0
while i_var < len(order_var):
    u_var = order_var[i_var]
    size_var = 1
    j_var = 0
    while j_var < len(adj_list_var[u_var]):
        v_var = adj_list_var[u_var][j_var]
        if v_var != parent_var[u_var]:
            size_var += subtree_var[v_var]
        j_var = j_var + 1
    subtree_var[u_var] = size_var
    i_var = i_var + 1

answers_var = []

queries_var = int(input())

i_var = 0

while i_var < queries_var:

    q_var = int(input())

    answers_var.append(subtree_var[q_var])

    i_var = i_var + 1

i_var = 0

while i_var < len(answers_var):

    print(answers_var[i_var])

    i_var = i_var + 1