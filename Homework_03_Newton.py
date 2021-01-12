import math

def newton_method(function, de_function, start_point):
	x = start_point
	while True:
		x_next = x - (function(x) / de_function(x))
		if abs(x_next-x) < 0.00001:
			return x_next
		else:
			x = x_next

# Demonstrate: This function should be custom
def function(x):
	return math.log(x) + 2.0 * x ** 2.0 - 3.0

# Demonstrate: This function should be custom
def de_function(x):
	return 4.0 * x + (1.0 / x)

# Demonstrate
if __name__ == '__main__':
	newton_method(function, de_function, start_point=0.5)