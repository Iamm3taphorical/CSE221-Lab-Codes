# PROBLEM: Build coprime graph and answer k-th neighbor queries
# INPUT: Multiple test cases, each with N nodes, Q queries, and queries asking for k-th coprime neighbor
# OUTPUT: For each query, print the k-th smallest coprime neighbor or -1 if doesn't exist
# KEYWORDS: coprime numbers, GCD, number theory, graph construction, neighbor queries

import sys  # fast stdin

input = sys.stdin.readline  # quick line reads

def gcd_var(a_var, b_var):  # Euclidean algorithm for greatest common divisor
    
    while b_var:  # continue until b becomes zero
        a_var, b_var = b_var, a_var % b_var  # simultaneous assignment: swap and mod
    return a_var  # when b is 0, a holds the GCD

# read number of test cases from first line
t_var = int(input())

# process each test case
while t_var > 0:

    N_var, Q_var = map(int, input().split())  # number of nodes and queries
    
    graph_var = []  # adjacency list where edges connect coprime node labels
    
    i_var = 1  # node label (1-based)
    while i_var <= N_var:  # build neighbors for each node label 1..N
    
        neighbors_var = []  # list of coprime neighbors for current node
    
        j_var = 1  # candidate neighbor label
        while j_var <= N_var:  # check all possible nodes
    
            if i_var != j_var and gcd_var(i_var, j_var) == 1:  # coprime (GCD=1) and not self-loop
                neighbors_var.append(j_var)  # add to neighbor list
    
            j_var = j_var + 1  # check next candidate
        
        graph_var.append(neighbors_var)  # store neighbors for node i_var (0-indexed storage)
        i_var = i_var + 1  # move to next node
    
    answers_var = []  # responses to queries for this test case
    
    i_var = 0  # query counter
    
    while i_var < Q_var:  # process each query
        
        node_var, k_var = map(int, input().split())  # node label and 1-based index of neighbor
    
        if k_var > len(graph_var[node_var - 1]):  # request out of bounds (kth neighbor doesn't exist)
    
            answers_var.append(-1)  # append -1 for invalid query
        else:
            answers_var.append(graph_var[node_var - 1][k_var - 1])  # get kth neighbor (convert to 0-based)
        
        i_var = i_var + 1  # next query
    
    i_var = 0  # reset for output loop
    
    while i_var < len(answers_var):  # output all answers for this test case
    
        print(answers_var[i_var])  # print one answer per line
    
        i_var = i_var + 1
    
    # move to next test case
    t_var = t_var - 1
