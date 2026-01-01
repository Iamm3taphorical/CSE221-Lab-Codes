import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

def gcd_var(a_var, b_var):  # Euclidean algorithm

    while b_var:
        a_var, b_var = b_var, a_var % b_var
    return a_var

N_var, Q_var = map(int, input().split())  # number of nodes and queries

graph_var = []  # adjacency list where edges connect coprime labels

i_var = 1
while i_var <= N_var:  # build neighbors for each node label 1..N

    neighbors_var = []

    j_var = 1
    while j_var <= N_var:

        if i_var != j_var and gcd_var(i_var, j_var) == 1:  # coprime and not self
            neighbors_var.append(j_var)

        j_var = j_var + 1
    graph_var.append(neighbors_var)  # store neighbors for node i_var
    i_var = i_var + 1

answers_var = []  # responses to queries

i_var = 0

while i_var < Q_var:  # process each query
    
    node_var, k_var = map(int, input().split())  # node label and 1-based index

    if k_var > len(graph_var[node_var - 1]):  # request out of bounds

        answers_var.append(-1)
    else:
        answers_var.append(graph_var[node_var - 1][k_var - 1])  # kth neighbor
    i_var = i_var + 1

i_var = 0

while i_var < len(answers_var):  # output all answers

    print(answers_var[i_var])

    i_var = i_var + 1