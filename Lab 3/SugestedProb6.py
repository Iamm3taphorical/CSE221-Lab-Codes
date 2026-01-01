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

result_var = []

def buildOrder_var(left_var, right_var):
    if left_var > right_var:
        return
    mid_var = (left_var + right_var) // 2
    result_var.append(a_var[mid_var])
    buildOrder_var(left_var, mid_var - 1)
    buildOrder_var(mid_var + 1, right_var)

buildOrder_var(0, n_var - 1)

for j_var in range(len(result_var)):
    if j_var != 0:
        sys.stdout.write(" ")
    sys.stdout.write(str(result_var[j_var]))

sys.stdout.write("\n")