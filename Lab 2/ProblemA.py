import sys

# Read all input data from standard input
data_var = sys.stdin.read().strip().split()

# Step 1: Parse the first two values
n_var = int(data_var[0])     # Number of elements in the list
s_var = int(data_var[1])     # Target sum value

# Step 2: Create the list (convert the next n_var items to integers)
arr_var = []
i_var = 2                    # Start reading from the 3rd item (0-based index 2)

while i_var < 2 + n_var:
    arr_var.append(int(data_var[i_var]))
    i_var = i_var + 1

# Step 3: Initialize two pointers
left_var = 0
right_var = n_var - 1

found_var = False             # To check if we found a valid pair

# Step 4: Two pointer search
while left_var < right_var:
    
    sum_var = arr_var[left_var] + arr_var[right_var]
    
    if sum_var == s_var:
        # Found a valid pair, print their 1-based indices
        sys.stdout.write(str(left_var + 1) + " " + str(right_var + 1) + "\n")
        found_var = True
        break
        
    elif sum_var < s_var:
        # Need a larger sum → move the left pointer right
        left_var = left_var + 1
        
    else:
        # Need a smaller sum → move the right pointer left
        right_var = right_var - 1

# Step 5: If no pair found
if not found_var:
    sys.stdout.write("-1\n")
