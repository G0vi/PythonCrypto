import sys
sys.setrecursionlimit(1000000)
from random import randint
        
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
        
def Fermat(n,time):
    for i in range(1, time):
        b = randint(1, n-1)
        d = gcd(b, n)
        if d != 1:
            return False
        if(pow(b,n-1,n) != 1):
            return False
    return True


