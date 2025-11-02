import sys

data_var = sys.stdin.read().strip().split("\n")

n_var = int(data_var[0])

trains_var = []

i_var = 1

while i_var <= n_var:
    
    line_var = data_var[i_var].strip()
    
    parts_var = line_var.split()
    
    name_var = parts_var[0]
    
    time_str_var = parts_var[-1]
    
    hr_var = int(time_str_var.split(":")[0])
    
    mn_var = int(time_str_var.split(":")[1])
    
    total_time_var = hr_var * 60 + mn_var
    
    trains_var.append((name_var, total_time_var, i_var - 1, line_var))
    
    i_var = i_var + 1


i_var = 0

while i_var < n_var:
    
    j_var = 0
    
    while j_var + 1 < n_var:
        
        name1_var = trains_var[j_var][0]
        
        time1_var = trains_var[j_var][1]
        
        idx1_var = trains_var[j_var][2]
        
        name2_var = trains_var[j_var + 1][0]
        
        time2_var = trains_var[j_var + 1][1]
        idx2_var = trains_var[j_var + 1][2]
        
        swap_flag_var = 0
        

        if name1_var > name2_var:
            
            swap_flag_var = 1
            
        elif name1_var == name2_var:
            
            if time1_var < time2_var:
                swap_flag_var = 1
            elif time1_var == time2_var:
                
                swap_flag_var = 0
        
        if swap_flag_var == 1:
            
            temp_var = trains_var[j_var]
            
            trains_var[j_var] = trains_var[j_var + 1]
            trains_var[j_var + 1] = temp_var
        
        j_var = j_var + 1
    
    i_var = i_var + 1


i_var = 0

while i_var < n_var:
    sys.stdout.write(trains_var[i_var][3] + "\n")
    i_var = i_var + 1
