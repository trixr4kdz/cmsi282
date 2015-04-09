name_map = {'T':20,'R':168,'I':131,'X':459,'E':2000,'O':765,'Q':1007,'U':313}

def verify(N, e, Md, M):
	if Md ** e % N == M:
		return True
	else:
		return False

def sign(M, d, N):
	return M**d % N

def print_orig_message(N, e, d, M):
	print '(M^d)^e = ' + str((M ** d) ** e % N)
	print 'MmodN = ' + str (M % N)