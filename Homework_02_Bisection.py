import math

def bisection(function, interval, precise=None):
	start = interval[0]
	end = interval[1]
	for i in range(100):
		middle = (start + end) / 2.0
		print(f'{i+1:3d}: {middle}')
		if precise is not None:
			if (end - start) < precise: return middle
		if function(middle) < 0:
			start = middle
			continue
		else:
			end = middle
	return middle

def fixed_point_iteration(function, start, precise=None):
	n = start
	for i in range(100):
		n_next = function(n)
		print(f'{i+1:3d}: {n_next}')
		if precise is not None:
			if abs(n_next - n) < precise: return n_next
		n = n_next
	return n_next

# For bisection, f(x); For FPI, g(x).
def function(x):
	return x**3.0 - 2.0*x + 2
	# return (2.0*x + 2.0)**(1./3.)

if __name__ == '__main__':
	answer = bisection(function, [0., 3.538])
	# answer = fixed_point_iteration(function, 2.0)
	# print(answer)