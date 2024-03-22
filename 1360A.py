t=int(input())
for i in range(t):
    a,b=[int(x) for x in input().split()]
    c=min(a,b)
    c=2*c
    c=max(a,b,c)
    print(c*c)