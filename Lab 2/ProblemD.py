import sys

data_var = sys.stdin.read().strip().split()
n_var = int(data_var[0])

a_var = []
b_var = []

i_var = 1
count_var = 0

while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1

m_var = int(data_var[i_var])
i_var = i_var + 1
count_var = 0

while count_var < m_var:
    b_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1

merged_var = []
left_var = 0
right_var = 0

while left_var < n_var and right_var < m_var:
    if a_var[left_var] <= b_var[right_var]:
        merged_var.append(a_var[left_var])
        left_var = left_var + 1
    else:
        merged_var.append(b_var[right_var])
        right_var = right_var + 1

while left_var < n_var:
    merged_var.append(a_var[left_var])
    left_var = left_var + 1

while right_var < m_var:
    merged_var.append(b_var[right_var])
    right_var = right_var + 1

i_var = 0
while i_var < len(merged_var):
    sys.stdout.write(str(merged_var[i_var]) + " ")
    i_var = i_var + 1

sys.stdout.write("\n")