def xgcd(a,b):
    if(a>b):
        k=1;
        
    else:
        k=0;
        c=a
        a=b 
        b=c 
    d1=0
    d2=1
    r=a%b
    c1=1 
    c2=-a//b
    while r>0:
        a=b
        b=r
        r=a%b
        q=a//b
        cur1=d1-q*c1
        cur2=d2-q*c2 
        d2=c2
        d1=c1
        c1=cur1;c2=cur2
    if(k==1):
        return [d1,d2+d1,b]
    else:
        return [d2+d1,d1,b]
def exgcd_back(a,b):
    Q=[]
    while(b!=0):
        Q.append(a//b)
        c=b
        b=a%b
        a=c
    Q.pop()
    p=-Q[-1];q=1
    for i in range(len(Q)-2,-1,-1):
        p1=q-p*Q[i]
        q=p
        p=p1
    return [q,p,a]
