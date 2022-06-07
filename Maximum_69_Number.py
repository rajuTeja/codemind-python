n=int(input())
l=list(str(n))
for i in range(len(l)):
    if l[i] == '6':
        l[i]=9
        break
for i in l:
    print(i,end='')