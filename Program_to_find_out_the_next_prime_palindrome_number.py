def palindrom(n):
    n1=n
    k=str(n)
    c=0
    for i in range(len(k)):
        m=n%10
        n=n//10
        c=c*10+m
    if c==n1 :
        return True
    else:
        return False
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return True
def gain(n):
    n+=1
    while palindrom(n)!=True or prime(n)!=True:
        n+=1
    else:
        return n
num=int(input())
print(gain(num))
'''num2=loss(num)
if abs(num-num1)>abs(num-num2):
    print(num2)
elif abs(num-num1)<abs(num-num2):
    print(num1)
else:
    print(num1,num2)'''