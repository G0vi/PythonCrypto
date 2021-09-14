# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)
from random import randint

'''def pow_own(a,b,n):
    ans=1
    a=a%n
    while(b!=0):
        if(b%2==1):
            ans=(ans*a)%n
        b//=2
        a=(a*a)%n
    return ans'''

def Miller_Rabin(n,time):
    k=0
    cur=n-1
    #找到k和q
    while(cur%2==0):
        k+=1
        cur//=2
    q=cur
    #考虑进行42次循环验证后，仍旧保持素数的性质，可以认为是素数
    for i in range(1,time):
        a=randint(1,n-1)
        flag=0
        if(pow(a,q,n)==1):
            flag=1
            continue
        for j in range(0,k+1):
            if(pow(a,int(2**j*q),n)==n-1):
                flag=1
                break
            #如果上述两个条件都不达成，那么就不是素数
        if(flag==0):
            return False
    return True

