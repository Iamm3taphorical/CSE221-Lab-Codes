n_var = int(input())
arr_var = list(map(int, input().split()))

def is_sorted_func(arr_check_var):
    i_var = 0
    while i_var < len(arr_check_var) - 1:
        if arr_check_var[i_var] > arr_check_var[i_var + 1]:
            return False
        i_var += 1
    return True


def reverse_func(arr_rev_var, start_var, moves_var):
    left_var = start_var
    right_var = start_var + 2
    

    while left_var < right_var:
        temp_var = arr_rev_var[left_var]
        arr_rev_var[left_var] = arr_rev_var[right_var]
        arr_rev_var[right_var] = temp_var
        
        left_var += 1
        right_var -= 1
    

    moves_var.append((start_var + 1, start_var + 3))

moves_var = []                
done_var = False              
iteration_var = 0             


if n_var <= 2:
    if is_sorted_func(arr_var):
        print("YES")
        print(0)
    else:
        print("NO")
else:
    while True:
        swapped_var = False
        i_var = 0
        
        while i_var <= n_var - 3:
            
            if arr_var[i_var] > arr_var[i_var + 1] or arr_var[i_var + 1] > arr_var[i_var + 2]:
                
                reverse_func(arr_var, i_var, moves_var)
                swapped_var = True
            
            i_var += 1
        
        if is_sorted_func(arr_var):
            done_var = True
            break
        
        if not swapped_var:
            break
        
        iteration_var += 1
        if iteration_var > n_var * 2:
            break   
    
    if done_var and is_sorted_func(arr_var):
        print("YES")
        print(len(moves_var))
        
        j_var = 0
        while j_var < len(moves_var):
            print(moves_var[j_var][0], moves_var[j_var][1])
            j_var += 1
    else:
        print("NO")