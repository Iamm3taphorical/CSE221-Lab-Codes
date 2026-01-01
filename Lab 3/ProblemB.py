import sys
from bisect import bisect_right, insort

data_var = sys.stdin.read().strip().split()
n_var = int(data_var[0])

array_var = []
i_var = 1
count_var = 0

while count_var < n_var:
    array_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1

result_var = 0
sorted_left_var = []

i_var = 0
while i_var < n_var:
    threshold_var = array_var[i_var] * array_var[i_var]
    index_var = bisect_right(sorted_left_var, threshold_var)
    result_var = result_var + (len(sorted_left_var) - index_var)
    insort(sorted_left_var, array_var[i_var])
    i_var = i_var + 1

sys.stdout.write(str(result_var) + "\n")