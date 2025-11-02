import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])

pos_var = 1

cnt_var = 0

while cnt_var < t_var:
    
    n_var = int(data_var[pos_var])
    
    pos_var += 1
    
    arr_var = []
    
    j_var = 0
    
    while j_var < n_var:
        arr_var.append(int(data_var[pos_var]))
        pos_var += 1
        j_var += 1
    
    k_var = 1
    flag_var = 1
    
    while k_var < n_var:
        if arr_var[k_var - 1] > arr_var[k_var]:
            flag_var = 0
            break
        k_var += 1
    
    if flag_var == 1:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
    
    cnt_var += 1