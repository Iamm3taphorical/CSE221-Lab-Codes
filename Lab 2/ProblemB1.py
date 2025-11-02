import sys

data_var = sys.stdin.read().strip().split()
n_var = int(data_var[0])
m_var = int(data_var[1])
k_var = int(data_var[2])

i_var = 3
a_var = []
b_var = []

count = 0
while count < n_var:
    a_var.append(int(data_var[i_var]))
    count = count + 1
    i_var = i_var + 1

count = 0
while count < m_var:
    b_var.append(int(data_var[i_var]))
    count = count + 1
    i_var = i_var + 1

left_var = 0
right_var = m_var - 1
best_i_var = 0
best_j_var = 0 
best_diff_var = float('inf')

while left_var < n_var and right_var >= 0:
    sum_var = a_var[left_var] + b_var[right_var]
    diff_var = abs(sum_var - k_var)

    if diff_var < best_diff_var: 
        best_diff_var = diff_var 
        best_i_var = left_var
        best_j_var = right_var


    if sum_var < k_var:
        left_var = left_var + 1
    else: 
        right_var = right_var - 1

sys.stdout.write(str(best_i_var + 1)+ " "+ str(best_j_var + 1) + "\n")