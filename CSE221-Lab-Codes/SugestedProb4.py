import sys
data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
array_var = list(map(int, data_var[1:]))

def count_odd_even(array_var):
    if len(array_var) == 1:
        if array_var[0] % 2 == 0:
            return (0, 1)
        else:
            return (1, 0)
    mid_var = len(array_var)//2
    left_odd, left_even = count_odd_even(array_var[:mid_var])
    right_odd, right_even = count_odd_even(array_var[mid_var:])
    return (left_odd + right_odd, left_even + right_even)

odd_var, even_var = count_odd_even(array_var)
print(odd_var, even_var)