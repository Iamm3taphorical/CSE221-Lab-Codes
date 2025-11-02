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
max_length_var = 0

freq_var = [0] * (n_var + 1)

distinct_count_var = 0

while right_var < n_var:
    curr_element_var = a_var[right_var]
    if freq_var[curr_element_var] == 0:
        distinct_count_var = distinct_count_var + 1
    freq_var[curr_element_var] = freq_var[curr_element_var] + 1

    while distinct_count_var > k_var:
        left_element_var = a_var[left_var]
        freq_var[left_element_var] = freq_var[left_element_var] - 1
        if freq_var[left_element_var] == 0:
            distinct_count_var = distinct_count_var - 1
        left_var = left_var + 1

    current_window_var = right_var - left_var + 1
    if current_window_var > max_length_var:
        max_length_var = current_window_var

    right_var = right_var + 1

sys.stdout.write(str(max_length_var) + "\n")