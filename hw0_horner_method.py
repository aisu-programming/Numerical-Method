def horner_method(x):
	answer = x + 1.0
	for _ in range(50): answer = answer * x + 1.0
	return answer

if __name__ == '__main__':
	answer = horner_method(1.0001)
	print(answer)