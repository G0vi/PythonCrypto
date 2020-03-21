from random import randint
import math
from .Fermat import Fermat
from .Miller_Rabin import Miller_Rabin

def isPrime(n):
    if Fermat(n, 50) and Miller_Rabin(n, 42):
        return True
    return False

def getPrime(nbit):
    while True:
        n = randint(2 ** (nbit - 1), 2 ** nbit)
        time = int(math.log(n)) * 4
        for i in range(time):
            if isPrime(n + i):
                return n + i
            if isPrime(n - i):
                return n - i
            
def nextPrime(n):
    cur = n + 1
    while not isPrime(cur):
        cur += 1
    return cur

