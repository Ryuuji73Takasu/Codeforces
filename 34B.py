n, m = map(int,input().split())
lst=list(map(int,input().split()))
summ=0
maxx=0

lst.sort()
for i in range(m):
    summ+=lst[i]
    if (summ<maxx):
        maxx=summ
print(-1*maxx)