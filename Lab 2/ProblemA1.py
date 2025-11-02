import sys 

data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])

s_var = int(data_var[1])

arr_var = []

i_var = 2

while i_var < 2+ n_var:

    arr_var.append(int(data_var[i_var]))

    i_var = i_var + 1

left_var = 0
right_var = n_var - 1
founder_var = False

while left_var < right_var: 

    sum_var = arr_var[left_var] + arr_var[right_var]

    if sum_var == s_var:
        sys.stdout.write(str(left_var +1) + " " + str(right_var + 1) + "\n")

        founder_var = True
        break

    elif sum_var > s_var:

        right_var = right_var - 1

    else:

        left_var = left_var + 1

if not founder_var:

    sys.stdout.write("-1\n")