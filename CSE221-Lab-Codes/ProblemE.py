import sys

input = sys.stdin.readline


def fast_power_mod(a, b, mod = 107):

    result = 1

    a = a % mod

    while b > 0:

        if b % 2 == 1:

            result = (result * a) % mod

        a = (a * a) % mod

        b = b // 2

    return result


def fast_series(a, n, m):

    if n == 0:

        return 0
    
    if n == 1:
        return a % m
    
    if n % 2 == 0:

        series_half = fast_series(a, n // 2, m)

        power_half = fast_power_mod(a, n // 2, m)

        return (series_half + (power_half * series_half) % m) % m
    
    else:

        return (fast_series(a, n - 1, m) + fast_power_mod(a, n, m)) % m


test_cases = int(input())

i_var = 0

while i_var < test_cases:

    a_var, n_var, m_var = map(int, input().split())

    sys.stdout.write(str(fast_series(a_var, n_var, m_var)) + "\n")

    i_var = i_var + 1