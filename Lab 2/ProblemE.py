import sys

data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
k_var = int(data_var[1])

a_var = []
i_var = 2
count_var = 0

while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1

left_var = 0
right_var = 0

current_sum_var = 0
max_length_var = 0

while right_var < n_var:
    current_sum_var = current_sum_var + a_var[right_var]

    while current_sum_var > k_var and left_var <= right_var:
        current_sum_var = current_sum_var - a_var[left_var]
        left_var = left_var + 1

    length_var = right_var - left_var + 1

    if current_sum_var <= k_var:
        if length_var > max_length_var:
            max_length_var = length_var

    right_var = right_var + 1

sys.stdout.write(str(max_length_var) + "\n")