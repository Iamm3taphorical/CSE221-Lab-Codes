import sys

data_var = sys.stdin.read().strip().split()
a_var = int(data_var[0])
n_var = int(data_var[1])

mod_var = 107

result_var = 1
a_var = a_var % mod_var

while n_var > 0:
    if n_var % 2 == 1:
        result_var = (result_var * a_var) % mod_var
    a_var = (a_var * a_var) % mod_var
    n_var = n_var // 2

sys.stdout.write(str(result_var) + "\n")