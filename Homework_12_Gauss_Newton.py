''' Keys '''
# x_0 = initial vector
# (D_r(x_k)^T x D_r(x_k)) x v = -D_r(x_k)^T x r(x_k)
# x_{k+1} = x_k + v


''' Libraries '''
import numpy as np
from hw04_05_LU_decomposition import get_answer


''' Codes '''
x1 = -1.
y1 = 0.
R1 = 1.

x2 = 1.
y2 = 1.
R2 = 1.

x3 = 1.
y3 = -1.
R3 = 1.

def r1(vector):
    x = vector[0]
    y = vector[1]
    return ((x - x1)**2 + (y - y1)**2)**0.5 - R1

def r2(vector):
    x = vector[0]
    y = vector[1]
    return ((x - x2)**2 + (y - y2)**2)**0.5 - R2

def r3(vector):
    x = vector[0]
    y = vector[1]
    return ((x - x3)**2 + (y - y3)**2)**0.5 - R3

def Dr(vector):
    x = vector[0]
    y = vector[1]
    S1 = ((x - x1)**2 + (y - y1)**2)**0.5
    S2 = ((x - x2)**2 + (y - y2)**2)**0.5
    S3 = ((x - x3)**2 + (y - y3)**2)**0.5
    return np.array([
        [ (x - x1) / S1, (y - y1) / S1 ], # dr1/x, dr1/y
        [ (x - x2) / S2, (y - y2) / S2 ], # dr2/x, dr2/y
        [ (x - x3) / S3, (y - y3) / S3 ], # dr3/x, dr3/y
    ])

def main():
    vector = np.array([0., 0.])
    for _ in range(20):
        r = np.array([ r1(vector), r2(vector), r3(vector) ])
        v = get_answer(
            np.dot(Dr(vector).transpose(), Dr(vector)),
            -1 * np.dot(Dr(vector).transpose(), r)
        )
        vector += v
    answer = vector
    print(answer, '\n')

if __name__ == "__main__":
    main()