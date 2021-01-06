''' Keys '''
# x_0 = initial vector
# x_{k+1} = x_k - ( (D_F(x_k))^{-1} x F(x_k) )
# s = -(D_F(x_k))^{-1} x F(x_k)   →   (D_F(x_k)) x s = -F(x_k)   →   可求 s


''' Libraries '''
import math
import numpy as np
from sklearn.linear_model import LinearRegression


''' Codes '''
def multivariate_newton_method(iv):
    v = iv
    for i in range(10):
        print(f'Turn {i+1:2d}: ', v)
        reg = LinearRegression(fit_intercept = False).fit(
            example_D_F(v[0], v[1], v[2]), -example_F(v[0], v[1], v[2])
        )
        v += reg.coef_
    return v

# Example
# f1() = x   + y   + z   - 3
# f2() = x^2 + y^2 + z^2 - 5
# f3() = e^x + xy  - xz  - 1
def example_D_F(x, y, z):

    element_0_0 = 1                  # d(f1)/dx
    element_0_1 = 1                  # d(f1)/dy
    element_0_2 = 1                  # d(f1)/dz

    element_1_0 = 2*x                # d(f2)/dx
    element_1_1 = 2*y                # d(f2)/dy
    element_1_2 = 2*z                # d(f2)/dz

    element_2_0 = math.e**x + y - z  # d(f3)/dx
    element_2_1 = x                  # d(f3)/dy
    element_2_2 = -1*x               # d(f3)/dz

    return np.array([
        [ element_0_0, element_0_1, element_0_2 ],
        [ element_1_0, element_1_1, element_1_2 ],
        [ element_2_0, element_2_1, element_2_2 ]
    ])

def example_F(x, y, z):
    element_0 = x + y + z - 3              # f1()
    element_1 = x**2 + y**2 + z**2 - 5     # f2()
    element_2 = math.e**x + x*y - x*z - 1  # f3()
    return np.array([ element_0, element_1, element_2 ])

if __name__ == "__main__":
    iv = [ 1, 1, 1 ] # initial vector
    print('')
    print('\nAnswer:  ', multivariate_newton_method(iv))