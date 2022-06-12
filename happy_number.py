def pd(n):
    r=0
    while n>0:
        t=n%10
        r+=(t*t)
        n=n//10
    return r
n=int(input())
while len (str(n))>1:
    k=pd (n)
    n=k
if k==1 or k==7:
    print(True)
else:
    print(False)