import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])

i_var = 1

while i_var <= t_var:
    
    n_var = int(data_var[i_var])
    
    res_var = (n_var * (n_var + 1)) // 2
    
    sys.stdout.write(str(res_var) + "\n")
    
    i_var += 1