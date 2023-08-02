import numpy as np
from math import sqrt

# _____________________ input size of matrix _______________________
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
#_________________________ check square matrix ______________________
if rows != cols:
    print("Error: The matrix must be square to calculate its cholesky.")
    exit()

#_________________________ input each element matrix ______________________
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)
#_________________________ check positive definit ______________________
for i in range (len(matrix)):
    if  matrix[i][i]<0 or np.all(np.linalg.eigvals(matrix)<0):
        print ('matrix not positive definite')
        exit()
    
    
#_________________________ input vector  ______________________
b = []
for i in range(rows):
    element = int(input(f"for vector enter(b{i+1}): "))
    b.append(element)
#_________________________ calculate R in cholesky  ______________________

def R_CALCULATE(A):
    n = len(A)
    # Create zero matrix for R
    r = [[0.0] * n for i in range(n)]
    #  Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(r[i][j] * r[k][j] for j in range(k))
            if (i == k): 
                r[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                r[i][k] = (1.0 / r[k][k] * (A[i][k] - tmp_sum))
    return r
#_________________________ calculate R inverse in cholesky  ______________________
def R_INVERSE_CALCULATE(A):
    r_inverse =[[0.0] * len(A) for i in range(len(A))]
    for i in range (len(A)):
        for j in range (len(A)):
            if i == j :
                r_inverse[i][j]= A[i][j]
            else :
                r_inverse [i][j] = A[j][i]
    return r_inverse
#___________________________Calculate R*y = b____________________________
r_matrix = R_CALCULATE(matrix)

y = []
for i in range (len (r_matrix)):
    y.append(0.0)
for i in range(len(r_matrix)):
    y[i] = b[i]
    for j in range(i):
        y[i] -=(r_matrix[i][j] * y[j] )
    y[i] /= r_matrix[i][i]

#___________________________Calculate R^-1x = y____________________________
r_inverse_matrix = R_INVERSE_CALCULATE(r_matrix)
def back_substitution(A, b):
    n = len(b)
    x = [0] * n
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
    return x

#___________________________ output ____________________________
output =(back_substitution(r_inverse_matrix,y))
for i in range(len(output)):
    print(f'x{i+1} = {output[i]}')
    print('____________________________________')
print(f'R matrix is :{r_matrix}')













