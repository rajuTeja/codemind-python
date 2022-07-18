n=int(input())
l=list(map(int,input().split()))
j=l[::-1]
for i in j:
    if i%2==0:
        k=(1+(j.index(i)))
        break
print(n-k)