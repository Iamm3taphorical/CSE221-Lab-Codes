import sys

data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])

a_var = []
i_var = 1
count_var = 0

while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    count_var = count_var + 1
    i_var = i_var + 1

best_square_var = a_var[0] * a_var[0]
best_i_var = 0

max_val_var = -float('inf')
best_j_var = 1

j_var = 1

while j_var < n_var:
    sum_var = best_square_var + (a_var[j_var] * a_var[j_var] * a_var[j_var])
    if sum_var > max_val_var:
        max_val_var = sum_var
        best_j_var = j_var
    if (a_var[j_var] * a_var[j_var]) > best_square_var:
        best_square_var = a_var[j_var] * a_var[j_var]
        best_i_var = j_var
    j_var = j_var + 1

sys.stdout.write(str(best_i_var) + " " + str(best_j_var) + "\n")