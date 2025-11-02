import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])
index_var = 1

while t_var > 0:
    k_var = int(data_var[index_var])
    x_var = int(data_var[index_var + 1])
    index_var = index_var + 2

    low_var = 1
    high_var = k_var * x_var

    while low_var < high_var:
        mid_var = (low_var + high_var) // 2
        count_var = mid_var - (mid_var // x_var)

        if count_var < k_var:
            low_var = mid_var + 1
        else:
            high_var = mid_var

    sys.stdout.write(str(low_var) + "\n")

    t_var = t_var - 1