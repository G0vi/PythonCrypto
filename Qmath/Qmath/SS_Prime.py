# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

from random import randint
from math import sqrt
#一下两个函数在求快速幂
def BCD_TO_BIN(a):
    l1=[]
    while(a):
        l1.append(a%2)
        a//=2
    return l1

def pow_new(a,b,n):
    a=a%n
    l1=BCD_TO_BIN(b)
    l2=[a]
    for i in range(1,len(l1)):
        l2.append((l2[-1]*l2[-1])%n)
    cur=1 
    for i in range(len(l1)):
        if(l1[i]):
            cur=(cur*l2[i])%n
    return cur
#求Jacobi   
def Jacobi(a,n):
    a=a%n
    #a=1,2,-1时直接公式得到
    if(a==0):
        return 0
    if(a==1):
        return 1
    if(a==2):
        return 1 if (n*n-1)%16==0 else -1
    if(a==n-1):
        return 1 if (n-1)%4==0 else -1
    li=[]
    cur=a
    #转换成一系列的乘积
    for i in range(2,int(sqrt(a))+1):
        if(cur%i==0):
            li.append([i,0])
            while(cur%i==0):
                li[-1][1]+=1
                cur//=i
            li[-1][1]=li[-1][1]%2
            #如果是2的倍数，那么直接等于1，约掉，不考虑
            if(li[-1][1]==0):
                li.pop()
    if(cur!=1):
        li.append([cur,1])
    #能分解为一系列的乘法
    if(len(li)>1):
        ans=1
        for j in li:
            ans*=Jacobi(j[0],n)
        return ans
    #自己已经无法再分解，进行二次互反律
    else:
        if(((n-1)*(a-1))%8==0):
            return Jacobi(n,a)
        else:
            return -Jacobi(n,a)

#判断是否是素数    
def SS_IsPrime(n):
    #进行52次判定后，可以大致确定是否是素数
    for i in range(1,52):
        b=randint(2,n-2)
        r=pow_new(b,int((n-1)/2),n)
        if(r!=1 and r!=n-1):
            return False
        s=Jacobi(b,n)
        if(r!=s):
            return False
    return True
