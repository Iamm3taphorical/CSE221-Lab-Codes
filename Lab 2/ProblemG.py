import sys

data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
q_var = int(data_var[1])

a_var = []
i_var = 2
count_var = 0

while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1

output_list_var = []

query_count_var = 0

while query_count_var < q_var:
    x_var = int(data_var[i_var])
    y_var = int(data_var[i_var + 1])
    i_var = i_var + 2

    
    left_var = 0
    right_var = n_var
    while left_var < right_var:
        mid_var = (left_var + right_var) // 2
        if a_var[mid_var] < x_var:
            left_var = mid_var + 1
        else:
            right_var = mid_var
    lower_bound_var = left_var

    left_var = 0
    right_var = n_var
    while left_var < right_var:
        mid_var = (left_var + right_var) // 2
        if a_var[mid_var] <= y_var:
            left_var = mid_var + 1
        else:
            right_var = mid_var
    upper_bound_var = left_var

    result_var = upper_bound_var - lower_bound_var
    output_list_var.append(str(result_var) + "\n")

    query_count_var = query_count_var + 1

sys.stdout.write("".join(output_list_var))