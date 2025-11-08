import sys
data_var = sys.stdin.read().strip().split()

a_var = int(data_var[0])
n_var = int(data_var[1])
mod_var = 107

def fast_power_mod(a_var, b_var, mod_var):
    res_var = 1
    a_var = a_var % mod_var
    while b_var > 0:
        if b_var % 2 == 1:
            res_var = (res_var * a_var) % mod_var
        a_var = (a_var * a_var) % mod_var
        b_var //= 2
    return res_var

def fast_series(a_var, n_var, mod_var):
    if n_var == 0:
        return 0
    if n_var == 1:
        return a_var % mod_var
    if n_var % 2 == 0:
        half_var = fast_series(a_var, n_var // 2, mod_var)
        pow_var = fast_power_mod(a_var, n_var // 2, mod_var)
        return (half_var * (1 + pow_var)) % mod_var
    else:
        return (fast_series(a_var, n_var - 1, mod_var) + fast_power_mod(a_var, n_var, mod_var)) % mod_var

print(fast_series(a_var, n_var, mod_var))