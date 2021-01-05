import math
import numpy as np
from sklearn.linear_model import LinearRegression


def multivariate_newton_method(iv):
    v = iv
    for i in range(10):
        print(f'Turn {i+1:2d}: ', v)
        reg = LinearRegression(fit_intercept = False).fit(
            D(v[0], v[1], v[2]), negative_F(v[0], v[1], v[2])
        )
        v += reg.coef_
    return v

def D(x, y, z):
    element_0_0 = 1
    element_0_1 = 1
    element_0_2 = 1
    element_1_0 = 2*x
    element_1_1 = 2*y
    element_1_2 = 2*z
    element_2_0 = math.e**x + y - z
    element_2_1 = x
    element_2_2 = -1*x
    return np.array([
        [ element_0_0, element_0_1, element_0_2 ],
        [ element_1_0, element_1_1, element_1_2 ],
        [ element_2_0, element_2_1, element_2_2 ]
    ])

def negative_F(x, y, z):
    element_0 = -1 * (x + y + z - 3)
    element_1 = -1 * (x**2 + y**2 + z**2 - 5)
    element_2 = -1 * (math.e**x + x*y - x*z - 1)
    return np.array([ element_0, element_1, element_2 ])

if __name__ == "__main__":

    # initial vector
    iv = [ 1, 1, 1 ]

    print('')
    print('\nAnswer: ', multivariate_newton_method(iv))