import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])

pos_var = 1

cnt_var = 0

while cnt_var < t_var:
    
    _skip_var = data_var[pos_var]
    
    a_str_var = data_var[pos_var + 1]
    
    op_var = data_var[pos_var + 2]
    
    b_str_var = data_var[pos_var + 3]
    
    a_var = float(a_str_var)
    
    b_var = float(b_str_var)
    
    if op_var == "+":
        res_var = a_var + b_var
    else:
        if op_var == "-":
            res_var = a_var - b_var
        else:
            if op_var == "*":
                res_var = a_var * b_var
            else:
                res_var = a_var / b_var
    
    sys.stdout.write("{:.6f}\n".format(res_var))
    
    pos_var += 4
    
    cnt_var += 1