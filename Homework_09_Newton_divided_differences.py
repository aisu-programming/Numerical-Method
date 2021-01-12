''' Keys '''
# P(x) = c0 + c1(x-x1) + c2(x-x1)(x-x2) + ... + c{n-1}(x-x1)...(x-x{n-1})

# P(x) = f(x1) + f[x1 x2](x-x1)(x-x2)
#              + f[x1 x2 x3](x-x1)(x-x2)(x-x3)
#              + ...
#              + f[x1 ... xn](x-x1)...(x-xn)

# f[x1] = P(x1) = y1
# f[x1 x2] = (f[x2] - f[x1]) / (x2 - x1)
# f[x1 x2 x3] = (f[x2 x3] - f[x1 x2]) / (x3 - x1)
# f[x1 x2 x3 x4] = (f[x2 x3 x4] - f[x1 x2 x3]) / (x4 - x1)


''' Libraries '''
import numpy as np


''' Codes '''
def customize_horner_method(C, X, target):
    answer = C[-1]
    for i in range(len(X)-1, 0, -1):
        answer = answer * (target - X[i-1]) + C[i-1]
    return answer

def example_newton_divided_differences():
    data = [ (1800, 280),
             (1850, 283),
             (1900, 291),
             (2000, 370), ]
    target = 1950

    X = np.array([ t[0] for t in data ])
    length = X.shape[0]
    Y = np.zeros((length, length))
    for i, _ in enumerate(Y[0]): Y[0][i] = data[i][1]
    for i in range(1, X.shape[0]+1):
        for j in range(X.shape[0] -i):
            Y[i][j] = (Y[i-1][j+1] - Y[i-1][j]) / (X[j+i] - X[j])

    coeff = [ c for c in Y[:, 0] ]
    # print(coeff)

    answer = customize_horner_method(coeff, X, target)
    print(answer)

if __name__ == "__main__":
    example_newton_divided_differences()