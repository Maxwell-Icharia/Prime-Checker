def is_prime(number):
	if number > 1:
		if number == 2:
			print True
		else:
			v = 2 ** number
			b = v % number
			if b == 2:
				print True
			else:
				print False