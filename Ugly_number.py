def ug(n,div):
    while (n %div==0):
        n=n//div
    return n
n=int(input())
n=ug(n,2)
n=ug(n,3)
n=ug(n,5)
if n==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')