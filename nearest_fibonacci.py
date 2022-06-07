def fb(n):
    l=[0,1]
    for i in range(n):
        l.append(sum(l[-2:]))
    return l
n=int(input())
n1=n
m=n
k,j=0,0
while n>=0:
    if n in fb(n):
        k=n
        break
    n=n-1
while n1>=0:
    if n1 in fb(n1):
        j=n1
        break
    n1=n1+1
if abs(m-k)>abs(m-j):
    print(j)
elif abs(m-j)>abs(m-k):
    print(k)
else:
    print(k,j)