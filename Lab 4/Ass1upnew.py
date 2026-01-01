# PROBLEM: Build and print adjacency list with weights for directed graphs (multiple test cases)
# INPUT: t test cases; for each: N (vertices), M (edges), then three arrays U, V, W of length M (u endpoints, v endpoints, weights)
# OUTPUT: For each test case, for each node 1..N, print "node: (v,w) (v,w)..." for its outgoing edges
# KEYWORDS: adjacency list, directed graph, weighted edges, graph representation, multiple test cases

import sys  # fast stdin/stdout

def main():
    data_var = sys.stdin.buffer.read().split()  # read all tokens at once for speed
    idx_var = 0  # token cursor
    out_lines_var = []  # collect all output lines across test cases

    t_var = int(data_var[idx_var]); idx_var += 1  # number of test cases

    tc_var = 0  # test case counter
    while tc_var < t_var:  # process each test case
        tc_var += 1  # advance test case index

        N_var = int(data_var[idx_var]); idx_var += 1  # number of vertices
        M_var = int(data_var[idx_var]); idx_var += 1  # number of edges

        U_var = [0] * M_var  # start nodes array
        V_var = [0] * M_var  # end nodes array
        W_var = [0] * M_var  # weights array

        mi_var = 0  # edge index for U
        while mi_var < M_var:  # read all U endpoints
            U_var[mi_var] = int(data_var[idx_var]); idx_var += 1
            mi_var += 1

        mi_var = 0  # edge index for V
        while mi_var < M_var:  # read all V endpoints
            V_var[mi_var] = int(data_var[idx_var]); idx_var += 1
            mi_var += 1

        mi_var = 0  # edge index for W
        while mi_var < M_var:  # read all weights
            W_var[mi_var] = int(data_var[idx_var]); idx_var += 1
            mi_var += 1

        adj_var = [[] for _ in range(N_var + 1)]  # adjacency list (1-based)

        ei_var = 0  # edge builder index
        while ei_var < M_var:  # populate adjacency list with (v, w)
            u_var = U_var[ei_var]  # source
            v_var = V_var[ei_var]  # destination
            w_var = W_var[ei_var]  # weight
            adj_var[u_var].append((v_var, w_var))  # add weighted edge
            ei_var += 1

        node_var = 1  # current node to print
        while node_var <= N_var:  # iterate all nodes
            line_parts_var = []  # hold formatted (v,w) pairs

            j_var = 0  # neighbor index
            neigh_var = adj_var[node_var]  # list of neighbors for this node
            ln_var = len(neigh_var)  # number of neighbors
            while j_var < ln_var:  # format each neighbor pair
                pair_var = neigh_var[j_var]  # (target, weight)
                line_parts_var.append("(" + str(pair_var[0]) + "," + str(pair_var[1]) + ")")  # format pair
                j_var += 1

            if line_parts_var:  # if node has outgoing edges
                out_lines_var.append(str(node_var) + ": " + " ".join(line_parts_var))  # node label + pairs
            else:  # no outgoing edges
                out_lines_var.append(str(node_var) + ":")  # node label only

            node_var += 1  # next node

    sys.stdout.write("\n".join(out_lines_var))  # emit all results at once

if __name__ == "__main__":
    main()