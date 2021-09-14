def modinv(m, N):
    from libnum import xgcd, gcd
    assert gcd(m, N) == 1
    return xgcd(m, N)[0] % N


def samod_attack((c1, c2), (e1, e2), N):
    from libnum import xgcd, gcd
    assert gcd(e1, e2) == 1
    assert gcd(e1, N) == 1
    assert gcd(e2, N) == 1
    [r, s] = xgcd(e1, e2)[0:2]
    cc1, cc2 = c1, c2
    if r < 0:
        r = -r
        cc1 = modinv(cc1, N)
    if s < 0:
        s = -s
        cc2 = modinv(cc2, N)
    m = pow(cc1, r, N) * pow(cc2, s, N) % N
    return m
