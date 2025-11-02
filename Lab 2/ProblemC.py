import sys 

data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
t_var = int(data_var[1])

a_var = []

i_var = 2

count_var = 0

while count_var < n_var:

    a_var.append((int(data_var[i_var]), count_var + 1))
    
    i_var = i_var + 1
    count_var = count_var + 1

a_var.sort()

found_var = False

i_var = 0

while i_var < n_var - 2:
    first_val_var = a_var[i_var][0]
    left_var = i_var + 1
    right_var = n_var - 1
    target_var = t_var - first_val_var

    while left_var < right_var:
        sum_var = a_var[left_var][0] + a_var[right_var][0]

        if sum_var == target_var:
            sys.stdout.write(str(a_var[i_var][1]) + " " + str(a_var[left_var][1]) + " " + str(a_var[right_var][1]) + "\n")
            found_var = True
            break

        elif sum_var < target_var:
            left_var = left_var + 1

        else:
            right_var = right_var - 1

    if found_var:
        break

    i_var = i_var + 1

if not found_var:
    sys.stdout.write("-1\n")