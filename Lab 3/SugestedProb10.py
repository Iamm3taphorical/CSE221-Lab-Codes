import sys

data_var = sys.stdin.read().strip().split()

mod_var = 1000000007

t_var = int(data_var[0])

index_var = 1

def multiply_var(a_var, b_var):
    result_var = [[0,0],[0,0]]
    i_var = 0
    while i_var < 2:
        j_var = 0
        while j_var < 2:
            k_var = 0
            while k_var < 2:
                result_var[i_var][j_var] = (result_var[i_var][j_var] + (a_var[i_var][k_var] * b_var[k_var][j_var])) % mod_var
                k_var = k_var + 1
            j_var = j_var + 1
        i_var = i_var + 1
    return result_var

def power_var(a_var, x_var):
    result_var = [[1,0],[0,1]]
    while x_var > 0:
        if x_var % 2 == 1:
            result_var = multiply_var(result_var, a_var)
        a_var = multiply_var(a_var, a_var)
        x_var = x_var // 2
    return result_var

count_var = 0
while count_var < t_var:
    a11 = int(data_var[index_var])
    a12 = int(data_var[index_var + 1])
    a21 = int(data_var[index_var + 2])
    a22 = int(data_var[index_var + 3])
    x_var = int(data_var[index_var + 4])
    index_var = index_var + 5

    matrix_var = [[a11, a12], [a21, a22]]

    res_var = power_var(matrix_var, x_var)

    sys.stdout.write(str(res_var[0][0]) + " " + str(res_var[0][1]) + "\n")
    sys.stdout.write(str(res_var[1][0]) + " " + str(res_var[1][1]) + "\n")

    count_var = count_var + 1