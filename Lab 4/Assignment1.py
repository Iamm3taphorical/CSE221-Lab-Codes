import sys  # access fast stdin/stdout

input = sys.stdin.readline  # faster line-based input

N_var , M_var = map(int , input().split())  # N vertices, M directed edges with weights

adjMatrix_var = []  # will store the N x N matrix
i_var = 0  # row counter

while i_var < N_var:  # build each row
    rowList_var = []  # current row placeholder
    
    j_var = 0  # column counter
    while j_var < N_var:  # fill row with zeros
        rowList_var.append(0)  # no edge yet
        j_var += 1  # move to next column
    
    adjMatrix_var.append(rowList_var)  # add completed row
    i_var += 1  # move to next row

k_var = 0  # edge counter
while k_var < M_var:  # read all edges
    u_var , v_var , w_var = map(int , input().split())  # endpoints (1-based) and weight
    
    adjMatrix_var[u_var - 1][v_var - 1] = w_var  # place weight in 0-based matrix position
    
    k_var += 1  # next edge

x_var = 0  # printing row index
while x_var < N_var:  # output the matrix
    
    print(*adjMatrix_var[x_var])  # print row as space-separated values
    
    x_var += 1  # next row
