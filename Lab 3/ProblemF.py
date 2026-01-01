import sys

input = sys.stdin.readline

def arranger(array_var):

    if len(array_var) == 0:

        return []
    
    mid_index_var = len(array_var) // 2

    root_var = array_var[mid_index_var]
    
    left_part_var = arranger(array_var[:mid_index_var])
    right_part_var = arranger(array_var[mid_index_var + 1:])
    
    result_var = [root_var]
    
    i_var = 0

    while i_var < len(left_part_var):
        result_var.append(left_part_var[i_var])
        i_var = i_var + 1
    
    j_var = 0

    while j_var < len(right_part_var):
        result_var.append(right_part_var[j_var])
        
        j_var = j_var + 1
    
    return result_var


array_size_var = int(input())
array_var = list(map(int, input().split()))

result_var = arranger(array_var)

k_var = 0
while k_var < len(result_var):
    sys.stdout.write(str(result_var[k_var]) + " ")
    k_var = k_var + 1