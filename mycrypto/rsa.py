import Qmath

def rsa(e, n, p, q, c):
    from libnum import n2s, xgcd, gcd
    assert p * q == n
    phi = (p - 1) * (q- 1)
    assert gcd(e, phi) == 1
    d = xgcd(e, phi)[0] % phi
    return n2s(pow(c, d, n))

def small_attack(e, c, n):
    k = 0
    while 1:
        cur = k * n + c
        if Qmath.root(cur, e) ** e == cur:
            return Qmath.root(cur, e)
        k+=1
