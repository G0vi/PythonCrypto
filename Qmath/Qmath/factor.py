from .BigInt import root
from .PrimeSift import siftPrime

def factorize(n):
    #phase 1
    primes = siftPrime(1000000)
    ans = []
    for eve in primes:
        if n % eve == 0:
            eve1 = [eve, 0]
            while n % eve == 0:
                n /=  eve
                eve1[1] += 1
            ans.append(eve1)
    if n != 1:
        ans.append([n, 1])
    if len(ans) > 1:
        return ans
    #phase 2
    ro = root(n, 2)
    i = 1
    cur = ro
    while 1:
        cur += 1
        if n % cur == 0:
            return [cur, n / cur]
        if cur - ro >= 1000000:
            print 'Failed, Mr Z.Y.P'
            return None
    
