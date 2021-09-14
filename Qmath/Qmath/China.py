from .xgcd import xgcd

def China(A,N):
    if(len(A) == len(N)):
        M_All = 1 
        for i in N:
            M_All *= i
        x=0
        for j in range(len(A)):
           m = N[j]
           M = M_All // m
           M1 = xgcd(m, M)[1]
           x += (M * M1 * A[j]) % M_All
           x = x % M_All
        return (x, M_All)
    else:
        print "Wrong Format!"
        return
