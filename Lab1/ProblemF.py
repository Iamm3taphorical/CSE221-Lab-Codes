import sys

data_var = sys.stdin.read().strip().split()
n_var = int(data_var[0])

arr_var = []

i_var = 1

while i_var <= n_var:
    
    arr_var.append(int(data_var[i_var]))
    i_var = i_var + 1


swap_flag_var = 1
while swap_flag_var == 1:

    swap_flag_var = 0
    i_var = 0

    while i_var + 1 < n_var:

        left_var = arr_var[i_var]
        right_var = arr_var[i_var + 1]

        
        if left_var % 2 == right_var % 2:

            
            if left_var > right_var:
                
                temp_var = arr_var[i_var]
                
                arr_var[i_var] = arr_var[i_var + 1]
                
                arr_var[i_var + 1] = temp_var
                
                swap_flag_var = 1

        i_var = i_var + 1

i_var = 0

while i_var < n_var:
    
    sys.stdout.write(str(arr_var[i_var]) + " ")
    
    i_var = i_var + 1
