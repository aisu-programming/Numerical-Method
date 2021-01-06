import os

import numpy as np
from sklearn.linear_model import LinearRegression

def LU_decomposition(X):

    P = np.identity(X.shape[0])
    L = np.zeros(X.shape)
    U = X

    for index_i, row_x in enumerate(U):

        for _ in range(len(U)-1):
            for index in range(len(U[index_i:]) - 1):
                if abs(U[index+index_i+1][index_i]) > abs(U[index+index_i][index_i]):
                    tmp = np.array(U[index+index_i])
                    U[index+index_i] = U[index+index_i+1]
                    U[index+index_i+1] = tmp
                    tmp = np.array(L[index+index_i])
                    L[index+index_i] = L[index+index_i+1]
                    L[index+index_i+1] = tmp
                    tmp = np.array(P[index+index_i])
                    P[index+index_i] = P[index+index_i+1]
                    P[index+index_i+1] = tmp

        for index_j, row_y in enumerate(U):
            if index_j > index_i:
                coef = float(row_y[index_i]) / float(row_x[index_i])
                L[index_j][index_i] = coef
                U[index_j] = row_y - row_x * coef
        
    L = L + np.identity(L.shape[0])
    return P, L, U

def get_answer(X, Y):
    reg = LinearRegression(fit_intercept = False).fit(X, Y)
    return reg.coef_

# Demonstrate:
if __name__ == "__main__":
    #                  x,     y,     z,     w
    X = np.array([[  4.0,   2.0,  -1.0,   3.0],
                  [  3.0,  -4.0,   2.0,   5.0],
                  [ -2.0,   6.0,  -5.0,  -2.0],
                  [  5.0,   1.0,   6.0,  -3.0]])
    Y = np.array( [ 16.9, -14.0,  25.0,   9.4])

    answer = get_answer(X, Y)
    P, L, U = LU_decomposition(X)
    
    print('Answer:')
    print(answer, '\n')
    print('P:')
    print(P, '\n')
    print('L:')
    print(L, '\n')
    print('U:')
    print(U)