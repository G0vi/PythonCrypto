
def Jacobi(a, b):
        from Qmath import gcd
        assert b & 1
	if a == b:
		return 0
	if a == 1:
		return 1
	if a == b - 1:
		if b % 4 == 1 or b == 2:
			return 1
		return -1
	if a == 2:
		if b % 8 == 1 or b % 8 == 7:
			return 1
		else:
			return -1
	if a & 1:
                mul = 1 if a % 4 == 1 or b % 4 == 1 else -1
		return mul * Jacobi(b % a, a) 
	ans = 1
	cur = factor_2(a)
	if cur[0] & 1:
                ans *= Jacobi(2, b)
        ans *= Jacobi(cur[1], b)
        return ans
	
import math

def factor_2(a):
        ans = 0
        cur = a
        while not cur & 1:
                ans += 1
                cur /= 2
        return ans, cur
        
def factor(a):
	ans = []
	store = a
	index = -1
	root = int(math.sqrt(store)) + 2
	for i in range(2, root):
		if store % i == 0:
			index += 1
			ans.append([i, 0])
		while store % i == 0:
			ans[index][1] += 1
			store /= i
	if store != 1:
	 	ans.append([store, 1])
	return ans
			
def Legendre(a, b):
	from Qmath import isPrime
	assert isPrime(b)
	if a == 1:
		return 1
	if a == b - 1:
		if b % 4 == 1 or b == 2:
			return 1
		return -1
	if a == 2:
		if b % 8 == 1 or b % 8 == 7:
			return 1
		else:
			return -1
	if isPrime(a):
		mul = 1 if a % 4 == 1 or b % 4 == 1 else -1
		return mul * Legendre(b % a, a)
	cur = factor(a)
	ans = 1
	for eve in cur:
		ans *= Legendre(eve[0], b) if eve[1] % 2 == 1 else 1
	return ans
def test(a,  b):
        for i in range(1, b):
                if pow(i, 2, b) == a:
                        return 1
        return -1
