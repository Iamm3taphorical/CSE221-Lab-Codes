import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])

i_var = 1

while i_var <= t_var:

    n_var = int(data_var[i_var])
    
    if n_var % 2 == 0:
        sys.stdout.write(str(n_var) + " is an Even number.\n")
    else:
        sys.stdout.write(str(n_var) + " is an Odd number.\n")
    
    i_var += 1