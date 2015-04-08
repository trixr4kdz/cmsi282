name_map = {'T':20,'R':168,'I':131,'X':459,'E':2000,'O':765,'Q':1007,'U':313}

def verify(N, e, Md, M):
	if Md ** e % N == M:
		return True
	else:
		print Md ** e % N
		return False

def sign(M, d, N):
	return M**d % N

def print_orig_message(N, e, d, M):
	print '(M^d)^e = ' + str((M ** d) ** e % N)
	print 'MmodN = ' + str (M % N)

print(sign(20, 2085, 2599))
print(verify(2599, 13, 2330, 20))

print_orig_message(2599, 13, 2085, 20)

print(sign(123, 2085, 2599)) # N = 2599, e = 13 so de = 1mod(112*22)--> d = 2085, p = 23, q = 113, relatively prime --> gcd(22*112, 13) = 1
print(verify(2599, 13, 312, 123)) # Should return true if 123 is the result when (M^d)^e mod N = M since d inverse of e