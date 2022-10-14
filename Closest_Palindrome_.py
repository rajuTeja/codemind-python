def palindrom(n):
    n1=n
    k=str(n)
    c=0
    for i in range(len(k)):
        m=n%10
        n=n//10
        c=c*10+m
    if c==n1:
        return True
    else:
        return False
def gain(n):
    n+=1
    while palindrom(n)!=True:
        n+=1
    else:
        return n
def loss(n):
    n-=1
    while palindrom(n)!=True:
        n-=1
    else:
        return n
num=int(input())
num1=gain(num)
num2=loss(num)
if abs(num-num1)>abs(num-num2):
    print(num2)
elif abs(num-num1)<abs(num-num2):
    print(num1)
else:
    print(num2,num1)