import numpy as np


def jacobi(A, b):
    answer_length = len(A)
    answer = np.zeros(answer_length)
    D_inverse = np.zeros((answer_length, answer_length)).astype(np.float32)
    L_plus_U = np.zeros((answer_length, answer_length)).astype(np.float32)
    for i in range(len(A)):
        D_inverse[i][i] = 1 / A[i][i]
        for j, e in enumerate(A[i]):
            if j != i: L_plus_U[i][j] = A[i][j]
    for _ in range(1000):
        answer = np.dot(D_inverse ,b - np.dot(L_plus_U, answer))
        # print(answer)
    return answer


def Gauss_Seidel(A, b):
    answer_length = len(A)
    answer = np.zeros(answer_length)
    D_inverse = np.zeros((answer_length, answer_length)).astype(np.float32)
    L_plus_U = np.zeros((answer_length, answer_length)).astype(np.float32)
    for i in range(len(A)):
        D_inverse[i][i] = 1 / A[i][i]
        for j, e in enumerate(A[i]):
            if j != i: L_plus_U[i][j] = A[i][j]
    for _ in range(1000):
        for i in range(answer_length):
            answer[i] = np.dot(D_inverse ,b - np.dot(L_plus_U, answer))[i]
        # print(answer)
    return answer


if __name__ == "__main__":

    # A
    # A = np.zeros((10, 10)).astype(np.float32)
    # for index in range(len(A)):
    #     if index != 0: A[index][index-1] = -1.0
    #     A[index][index] = 3.0
    #     if index != len(A)-1: A[index][index+1] = -1.0
    A = np.array([
        [ 2., -1.,  0.],
        [-1.,  2., -1.],
        [ 0., -1.,  2.]
    ])
    
    # b
    # b = np.ones(10).astype(np.float32)
    # b[0] = 2
    # b[-1] = 2
    b = np.array([0., 2., 0.])

    print(jacobi(A, b))
    print(Gauss_Seidel(A, b))