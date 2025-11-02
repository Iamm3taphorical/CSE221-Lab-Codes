import sys

data_var = sys.stdin.read().strip().split()

pos_var = 0

t_var = int(data_var[pos_var])

pos_var = pos_var + 1

out_lines_var = []

tc_var = 0

while tc_var < t_var:

    n_var = int(data_var[pos_var])
    pos_var = pos_var + 1

    ids_var = []
    i_var = 0
    while i_var < n_var:
        ids_var.append(int(data_var[pos_var + i_var]))
        i_var = i_var + 1
    pos_var = pos_var + n_var

    marks_var = []
    i_var = 0
    
    while i_var < n_var:
        marks_var.append(int(data_var[pos_var + i_var]))
        i_var = i_var + 1
    pos_var = pos_var + n_var

    pairs_var = []
    i_var = 0
    
    while i_var < n_var:
        pairs_var.append((ids_var[i_var], marks_var[i_var]))
        i_var = i_var + 1


    target_var = pairs_var[:]
    i_var = 0
    
    while i_var < n_var:
        j_var = 0
        while j_var + 1 < n_var:
            left_id_var, left_mark_var = target_var[j_var]
            right_id_var, right_mark_var = target_var[j_var + 1]

    
            need_swap_var = 0
            
            if right_mark_var > left_mark_var:
                need_swap_var = 1
            elif right_mark_var == left_mark_var:
                if right_id_var < left_id_var:
                    need_swap_var = 1

            if need_swap_var == 1:
                tmp_var = target_var[j_var]
                target_var[j_var] = target_var[j_var + 1]
                target_var[j_var + 1] = tmp_var

            j_var = j_var + 1
        i_var = i_var + 1


    id_to_target_idx_var = {}
    i_var = 0
    
    while i_var < n_var:
        id_to_target_idx_var[target_var[i_var][0]] = i_var
        i_var = i_var + 1


    perm_var = [0] * n_var
    i_var = 0
    
    while i_var < n_var:
        cur_id_var = pairs_var[i_var][0]
        perm_var[i_var] = id_to_target_idx_var[cur_id_var]
        i_var = i_var + 1

    
    visited_var = [0] * n_var
    min_swaps_var = 0
    i_var = 0
    
    while i_var < n_var:
        if visited_var[i_var] == 0:
            
            cycle_len_var = 0
            cur_var = i_var
            while visited_var[cur_var] == 0:
                visited_var[cur_var] = 1
                cycle_len_var = cycle_len_var + 1
                cur_var = perm_var[cur_var]
            if cycle_len_var > 0:
                min_swaps_var = min_swaps_var + (cycle_len_var - 1)
        i_var = i_var + 1


    out_lines_var.append("Minimum swaps: " + str(min_swaps_var))

    i_var = 0
    
    while i_var < n_var:
        
        out_lines_var.append("ID: " + str(target_var[i_var][0]) + " Mark: " + str(target_var[i_var][1]))
        i_var = i_var + 1

    tc_var = tc_var + 1

i_var = 0

while i_var < len(out_lines_var):
    
    sys.stdout.write(out_lines_var[i_var] + ("\n" if i_var < len(out_lines_var) - 1 else ""))
    i_var = i_var + 1
