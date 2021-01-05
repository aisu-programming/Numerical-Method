import numpy as np

def Gram_Schmidt_orthogonalization(matrix):
    Y = np.zeros(matrix.shape)
    Q = np.zeros(matrix.shape)
    R = np.zeros((matrix.shape[1], matrix.shape[1]))

    for i in range(len(Y)):
        Y[i] = A[i]
        for j in range(i):
            Y[i] -= np.dot(Q[j], np.dot(np.matrix.transpose(Q[j]), A[i]))
        Q[i] = Y[i] / np.linalg.norm(Y[i])

    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if i == j: R[i][j] = np.linalg.norm(Y[i])
            elif i < j: R[i][j] = np.dot(np.matrix.transpose(Q[i]), A[j])

    return Q, R

if __name__ == "__main__":
    A = np.array([
        [ 4.,  0.,  3.], # A1
        [ 8.,  2.,  6.], # A2
        [ 1., -2.,  7.], # A3
    ])
    Q, R = Gram_Schmidt_orthogonalization(A)

    print('Q:')
    print(Q)
    print('\nR:')
    print(R)