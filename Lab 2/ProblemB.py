# -----------------------------------------------------
# Problem: Two Sum Revisited
# Language: Python
import sys


data_var = sys.stdin.read().strip().split()


# -----------------------------------------------------
# Step 1: Extract Initial Inputs
# -----------------------------------------------------
n_var = int(data_var[0])
m_var = int(data_var[1])
k_var = int(data_var[2])


# -----------------------------------------------------
# Step 2: Read Array A and Array B
# -----------------------------------------------------
a_var = []
b_var = []

i_var = 3

# Reading array A
count_var = 0
while count_var < n_var:
    a_var.append(int(data_var[i_var]))
    count_var = count_var + 1
    i_var = i_var + 1


# Reading array B
count_var = 0
while count_var < m_var:
    b_var.append(int(data_var[i_var]))
    count_var = count_var + 1
    i_var = i_var + 1


# -----------------------------------------------------
# Step 3: Initialize Pointers and Tracking Variables
# -----------------------------------------------------
left_var = 0
right_var = m_var - 1

best_i_var = 0
best_j_var = 0
best_diff_var = float('inf')


# -----------------------------------------------------
# Step 4: Two-Pointer Traversal
# -----------------------------------------------------
while left_var < n_var and right_var >= 0:
    
    sum_var = a_var[left_var] + b_var[right_var]
    
    diff_var = abs(sum_var - k_var)
    
    
    # If this is closer to K, update the best pair
    if diff_var < best_diff_var:
        best_diff_var = diff_var
        best_i_var = left_var
        best_j_var = right_var
    
    
    # Move pointers
    if sum_var > k_var:
        right_var = right_var - 1
    else:
        left_var = left_var + 1



# -----------------------------------------------------
# Step 5: Output Result (1-based indices)
# -----------------------------------------------------
sys.stdout.write(str(best_i_var + 1) + " " + str(best_j_var + 1) + "\n")
