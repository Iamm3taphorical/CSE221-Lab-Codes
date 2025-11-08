import sys

data_var = sys.stdin.read().strip().split()

t_var = int(data_var[0])

index_var = 1

def power_var(a_var, b_var, mod_var):
    result_var = 1
    a_var = a_var % mod_var
    while b_var > 0:
        if b_var % 2 == 1:
            result_var = (result_var * a_var) % mod_var
        a_var = (a_var * a_var) % mod_var
        b_var = b_var // 2
    return result_var

def series_var(a_var, n_var, mod_var):
    if n_var == 0:
        return 0
    if n_var == 1:
        return a_var % mod_var
    if n_var % 2 == 0:
        half_var = series_var(a_var, n_var // 2, mod_var)
        p_var = power_var(a_var, n_var // 2, mod_var)
        return (half_var + (p_var * half_var) % mod_var) % mod_var
    else:
        return (series_var(a_var, n_var - 1, mod_var) + power_var(a_var, n_var, mod_var)) % mod_var

count_var = 0
while count_var < t_var:
    a_var = int(data_var[index_var])
    n_var = int(data_var[index_var + 1])
    m_var = int(data_var[index_var + 2])
    index_var = index_var + 3
    ans_var = series_var(a_var, n_var, m_var)
    sys.stdout.write(str(ans_var) + "\n")
    count_var = count_var + 1