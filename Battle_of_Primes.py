def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return True
n1=int(input())
n2=int(input())
m=n1+n2+1
c=1
while prime(m)==False:
    m+=1
    c+=1
else:
    print(c)