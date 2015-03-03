def lcm (x, y):
	return x * y / gcd (x, y)

def gcd(x, y):
	while (y != 0):
		x, y = y, x % y
		if (y == 0):
			return x
		else:
			gcd (x, y)