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

max_sum_var = -float('inf')
current_sum_var = 0

i_var = 0

while i_var < n_var:
    current_sum_var = current_sum_var + a_var[i_var]
    if current_sum_var > max_sum_var:
        max_sum_var = current_sum_var
    if current_sum_var < 0:
        current_sum_var = 0
    i_var = i_var + 1

sys.stdout.write(str(int(max_sum_var)))