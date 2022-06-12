def ds(n):
    k=0
    n=str(n)
    for i in range(len(n)):
        k+=int(n[i])**(i+1)
    return k
n=int(input())
print(ds(n)==n)
