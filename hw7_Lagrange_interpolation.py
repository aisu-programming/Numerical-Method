def item(data, k, target):
    numerator = 1
    denominator = 1
    for i in range(len(data)):
        if i == k: continue
        numerator *= (target - data[i][0])          # target - x_all_others
        denominator *= (data[k][0] - data[i][0])    # x_k    - x_all_others
    return data[k][1] * numerator / denominator     # y_k * all(target - x_all_others) / all(x_k - x_all_others)

def lagrange_interpolation():
    data = [ (1960, 3039585530),
             (1970, 3707475887),
             (1990, 5281653820),
             (2000, 6079603571) ]
    target = 1980

    answer = 0
    for i in range(len(data)):
        answer += item(data, i, target)

    print(answer)

if __name__ == "__main__":
    lagrange_interpolation()