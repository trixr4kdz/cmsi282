def compute (a, b, c, p):
	power = b * c
	return modPow (a, power, p)

def modPow(a, b, c):
    result = 1
    while b > 0:
        if isOdd(b):
            result = (result * a) % c
        a = (a * a) % c
        b >>= 1
    return result

def isOdd(x):
	return x % 2 == 1