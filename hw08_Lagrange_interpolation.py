''' Keys '''
# P(x)   = y_1 x L_1(x) + y_2 x L_2(x) + ... + y_n x L_n(x)
# L_k(x) = ((x-x_1) x ... x (x-x_{k-1}) x (x-x_{k+1}) x ... x (x-x_n)) / ((x_k-x_1) x ... x (x_k-x_{k-1}) x (x_k-x_{k+1}) x ... x (x_k-x_n))


''' Codes '''
def L_k(data, k, target):
    numerator = 1
    denominator = 1
    for i in range(len(data)):
        if i == k: continue
        numerator *= (target - data[i][0])          # target - x_all_others
        denominator *= (data[k][0] - data[i][0])    # x_k    - x_all_others
    return data[k][1] * numerator / denominator     # y_k * all(target - x_all_others) / all(x_k - x_all_others)

def example_lagrange_interpolation():
    data = [ (1960, 3039585530),
             (1970, 3707475887),
             (1990, 5281653820),
             (2000, 6079603571), ]
    target = 1980

    answer = 0
    for i in range(len(data)):
        answer += L_k(data, i, target)

    print(answer)

if __name__ == "__main__":
    example_lagrange_interpolation()