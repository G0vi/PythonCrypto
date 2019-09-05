from math import sqrt
def Arado_original(n):
    #all_number=list(range(2,n+1))
    test=[True]*(n+2)
    for i in range(2,int(sqrt(n))+1):
        if(test[i]):
            for j in range(i,n//i+1):
                test[j*i]=False
    sushu=[]
    for i in range(2,n+1):
        if(test[i]):
            sushu.append(i)
    return  sushu
    
def Arado(n):
    if(n>3):
        cur=Arado(int(sqrt(n)))
        test=[True]*(n+2)
        for eve in cur:
            for j in range(max(eve,int(sqrt(n))//eve),n//eve+1):
                test[eve*j]=False
        
        for i in range(int(sqrt(n))+1,n+1):
            if(test[i]):
                cur.append(i)
    else:
        cur=Arado_original(n)
    return cur
def Euler(n):
    test=[True]*(n+2)
    ans=[]
    for i in range(2,n+1):
        if(test[i]):
            ans.append(i)
        for j in ans:
            if(i * j > n):
                break;
            test[i*j] = False
            if(i%j==0):
                break
    return ans
def siftPrime(n):
    if n>1000:
        return Euler(n)
    return Arado(n)
