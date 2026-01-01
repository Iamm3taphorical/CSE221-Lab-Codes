import sys
data_var = sys.stdin.read().strip().split()

n_var = int(data_var[0])
words_var = data_var[1:]

def merge_count(left_dict, right_dict):
    for key in right_dict:
        if key in left_dict:
            left_dict[key] += right_dict[key]
        else:
            left_dict[key] = right_dict[key]
    return left_dict

def divide_count(words_var):
    if len(words_var) == 1:
        return {words_var[0]: 1}
    mid_var = len(words_var) // 2
    left_var = divide_count(words_var[:mid_var])
    right_var = divide_count(words_var[mid_var:])
    return merge_count(left_var, right_var)

freq_var = divide_count(words_var)
max_word = ""
max_count = 0

for k in freq_var:
    if freq_var[k] > max_count:
        max_count = freq_var[k]
        max_word = k

print(max_word)