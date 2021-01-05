''' Libraries '''
import math
import numpy as np

from hw3_4_LU_decomposition import get_answer


''' Constants '''
PI = math.pi


''' Codes '''
def predict_1(X, Y):
    A = np.array([
        [1, math.cos(2.0*PI*(x/12)), math.sin(2.0*PI*(x/12)), math.cos(4.0*PI*(x/12))] for x in X
    ])
    coeff = get_answer(np.dot(A.transpose(), A), np.dot(A.transpose(), Y))
    pred_Y = np.dot(A, coeff)
    return coeff, pred_Y

def predict_2(X, Y):
    A = np.array([
        [ 1, (x-1961) ] for x in X
    ])
    lnY = np.array([ math.log(y) for y in Y ])
    coeff = get_answer(np.dot(A.transpose(), A), np.dot(A.transpose(), lnY))
    pred_Y = np.array([ math.exp(y) for y in np.dot(A, coeff) ])
    return coeff, pred_Y

def euclidean_length(predict, Y):
    pass

def MSE(pred_Y, Y):
    total = 0
    for i in range(len(Y)): total += (pred_Y[i] - Y[i])**2.0
    return total

def RMSE(pred_Y, Y):
    rmse = (MSE(pred_Y, Y) / len(Y))**0.5
    return rmse


''' Demonstration '''
def question_1():
    X = np.array([ i for i in range(0, 12) ])
    Y = np.array([
        6.224,
        6.665,
        6.241,
        5.302,
        5.073,
        5.127,
        4.994,
        5.012,
        5.108,
        5.377,
        5.510,
        6.372,
    ])
    coeff, pred_Y = predict_1(X, Y)
    print(coeff)
    print(RMSE(pred_Y, Y))

def question_2():
    X = np.array([ i for i in range(0, 50) ])
    Y = np.array([
        320.58,
        321.01,
        322.25,
        322.24,
        322.16,
        324.01,
        325.00,
        325.57,
        327.34,
        328.07,
        328.92,
        330.07,
        332.48,
        333.09,
        333.97,
        334.87,
        336.75,
        338.01,
        339.47,
        341.46,
        342.91,
        344.14,
        345.75,
        347.43,
        348.93,
        350.21,
        351.84,
        354.22,
        355.67,
        357.16,
        359.34,
        359.66,
        360.28,
        361.68,
        363.79,
        365.41,
        366.80,
        369.30,
        371.00,
        371.82,
        374.02,
        375.55,
        378.35,
        380.61,
        382.24,
        384.94,
        386.43,
        388.49,
        390.18,
        393.22,
    ])
    Y = np.array([ (y-279) for y in Y ])
    coeff, pred_Y = predict_2(X, Y)
    print(math.exp(coeff[0]), coeff[1])
    print(pred_Y)
    print(RMSE(pred_Y, Y))

if __name__ == "__main__":
    question_1()
    # question_2()