n, k, w = map(int,input().split(" ",3))

if (w*(w+1)/2)*n-k>0:
    print(int((w*(w+1)/2)*n-k))
else:
    print(0)
