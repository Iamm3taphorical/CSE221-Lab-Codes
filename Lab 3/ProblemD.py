import sys

data_var = sys.stdin.read().strip().split()

index_var = 0

test_cases_var = int(data_var[index_var])

index_var = index_var + 1

mod_var = 1000000007

for _ in range(test_cases_var):
    a11_var = int(data_var[index_var]); index_var = index_var + 1

    a12_var = int(data_var[index_var]); index_var = index_var + 1

    a21_var = int(data_var[index_var]); index_var = index_var + 1

    a22_var = int(data_var[index_var]); index_var = index_var + 1

    exponent_var = int(data_var[index_var]); index_var = index_var + 1

    matrix_var = [[a11_var, a12_var], [a21_var, a22_var]]

    result_var = [[1, 0], [0, 1]]

    while exponent_var > 0:

        if exponent_var % 2 == 1:

            temp_var = [[0, 0], [0, 0]]

            for i in range(2):

                for j in range(2):
                    for k in range(2):
                        temp_var[i][j] += result_var[i][k] * matrix_var[k][j]
                        temp_var[i][j] %= mod_var
            result_var = temp_var
        temp_matrix_var = [[0, 0], [0, 0]]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    temp_matrix_var[i][j] += matrix_var[i][k] * matrix_var[k][j]
                    temp_matrix_var[i][j] %= mod_var
        matrix_var = temp_matrix_var
        exponent_var //= 2

    sys.stdout.write(str(result_var[0][0]) + " " + str(result_var[0][1]) + "\n")
    sys.stdout.write(str(result_var[1][0]) + " " + str(result_var[1][1]) + "\n")