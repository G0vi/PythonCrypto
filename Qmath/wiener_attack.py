def continued_fractions_expansion(numerator, denominator):  # (e,N)
    result = []
    divident = numerator % denominator
    quotient = numerator / denominator
    result.append(quotient)
    while divident != 0:
        numerator = numerator - quotient * denominator
        tmp = denominator
        denominator = numerator
        numerator = tmp
        divident = numerator % denominator
        quotient = numerator / denominator
        result.append(quotient)
    return result


def convergents(expansion):
    convergents = [(expansion[0], 1)]
    for i in range(1, len(expansion)):
        numerator = 1
        denominator = expansion[i]
        for j in range(i - 1, -1, -1):
            numerator += expansion[j] * denominator
            if j == 0:
                break
            tmp = denominator
            denominator = numerator
            numerator = tmp
        convergents.append((numerator, denominator))  # (k,d)
    return convergents


def newtonSqrt(n):
    approx = n / 2
    better = (approx + n / approx) / 2
    while better != approx:
        approx = better
        better = (approx + n / approx) / 2
    return approx


def wiener_attack(e, N):
    from random import randint
    from libnum import gcd
    cons = convergents(continued_fractions_expansion(e, N))
    for cs in cons:
        k, d = cs
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi_N = (e * d - 1) / k
        '''flag = 0
        for i in range(40):
            a = randint(2, N)
            if gcd(a, N) != 1:
                print a
            if pow(a, phi_N, N) != 1:
                flag = 1
                break
        if flag == 0:
            return phi_N'''
        
        # x**2-((N-phi_N)+1)*x+N=0
        a = 1
        b = -((N - phi_N) + 1)
        c = N
        delta = b * b - 4 * a * c
        if delta <= 0:
            continue
        x1 = (newtonSqrt(delta) - b) / (2 * a)
        x2 = -(newtonSqrt(delta) + b) / (2 * a)
        if x1 * x2 == N:
            return [x1, x2, k, d]
