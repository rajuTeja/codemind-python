def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return True
def rev(n):
    n1=str(n)
    reverse=0
    for i in range(len(n1)):
        m=n%10
        n=n//10
        reverse=reverse*10+m
    return reverse
jhon=int(input())
javid=rev(jhon)
if prime(jhon)==True:
    if prime(javid)==True:
        print('circular prime')
    else:
        print('prime but not a circular prime')
elif prime(javid)==True:
    print('prime but not a circular prime')
else:
    print('not prime')