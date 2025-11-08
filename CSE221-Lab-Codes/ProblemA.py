import sys

data_var = sys.stdin.read().strip().split()
n_var = int(data_var[0])
a_var = []
i_var = 1
count_var = 0

while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    i_var = i_var + 1
    count_var = count_var + 1


def merge(a_var, b_var):
    merged_var = []
    i_var = 0
    j_var = 0
    inv_count_var = 0

    while i_var < len(a_var) and j_var < len(b_var):
        if a_var[i_var] <= b_var[j_var]:
            merged_var.append(a_var[i_var])
            i_var = i_var + 1
        else:
            merged_var.append(b_var[j_var])
            j_var = j_var + 1
            inv_count_var = inv_count_var + (len(a_var) - i_var)

    while i_var < len(a_var):
        merged_var.append(a_var[i_var])
        i_var = i_var + 1

    while j_var < len(b_var):
        merged_var.append(b_var[j_var])
        j_var = j_var + 1

    return merged_var, inv_count_var


def mergeSort(arr_var):
    if len(arr_var) <= 1:
        return arr_var, 0

    mid_var = len(arr_var) // 2

    left_sorted_var, left_inv_var = mergeSort(arr_var[:mid_var])
    right_sorted_var, right_inv_var = mergeSort(arr_var[mid_var:])

    merged_var, cross_inv_var = merge(left_sorted_var, right_sorted_var)

    total_inv_var = left_inv_var + right_inv_var + cross_inv_var

    return merged_var, total_inv_var


sorted_arr_var, total_inversions_var = mergeSort(a_var)

sys.stdout.write(str(total_inversions_var) + "\n")

i_var = 0
while i_var < len(sorted_arr_var):
    sys.stdout.write(str(sorted_arr_var[i_var]) + " ")
    i_var = i_var + 1