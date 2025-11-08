import sys
data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
array_var = list(map(int, data_var[1:]))

def merge_zero(left_var, right_var):
    merged_var = []
    for val in left_var + right_var:
        if val != 0:
            merged_var.append(val)
    for val in left_var + right_var:
        if val == 0:
            merged_var.append(val)
    return merged_var

def divide_zero(array_var):
    if len(array_var) <= 1:
        return array_var
    mid_var = len(array_var)//2
    left_var = divide_zero(array_var[:mid_var])
    right_var = divide_zero(array_var[mid_var:])
    return merge_zero(left_var, right_var)

result_var = divide_zero(array_var)
print(*result_var)