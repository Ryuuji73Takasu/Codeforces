t = int(input())


for _ in range(t):
    n, k = map(int,input().split())
    a = []
    b = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(k):
        if (b[n-i-1]>a[i]):
            a[i]=b[n-i-1]
        else:
            break
    print(sum(a))