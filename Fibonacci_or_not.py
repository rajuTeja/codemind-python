def fb(n):
    l=[0,1]
    for i in range(n):
        l.append(sum(l[-2:]))
    return l
n=int(input())
if n in fb(n):
    print(True)
else:
    print(False)