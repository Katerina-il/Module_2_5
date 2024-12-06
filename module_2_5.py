def get_matrix(n, m, value):

matrix = []

for i in range(1, int(n) + 1):

if i > 0:

matrix_1 = []

matrix.append(matrix_1)

for j in range(1, int(m) + 1):

if j > 0:

matrix_1.append (value)

else:

break

return matrix



result_1 = get_matrix(2, 2, 10)

result_2 = get_matrix(3, 5, 42)

result_3 = get_matrix(4, 2, 13)

print(result_1, res ult_2, result_3)