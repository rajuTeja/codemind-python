n=int(input())
l=list(map(int,input().split()))
s=sum(l)
avg=s//n
fc=0
for i in l:
    if i<=avg:
        fc+=1
print(fc)