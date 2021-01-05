import numpy as np

def customize_horner_method(C, X, target):
    answer = C[-1]
    for i in range(len(X)-1, 0, -1):
        answer = answer * (target - X[i-1]) + C[i-1]
    return answer

def newton_divided_differences():
    data = [ (1800, 280),
             (1850, 283),
             (1900, 291),
             (2000, 370) ]
    target = 1950

    X = np.array([ t[0] for t in data ])
    length = X.shape[0]
    Y = np.zeros((length, length))
    for i, _ in enumerate(Y[0]): Y[0][i] = data[i][1]
    for i in range(1, X.shape[0]+1):
        for j in range(X.shape[0] -i):
            Y[i][j] = (Y[i-1][j+1] - Y[i-1][j]) / (X[j+i] - X[j])

    coeff = [ c for c in Y[:, 0] ]

    answer = customize_horner_method(coeff, X, target)
    print(answer)

if __name__ == "__main__":
    newton_divided_differences()