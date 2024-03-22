n = int(input())
a = list(map(int, 
    input().strip().split()))[:n]
count=1
result=1
for i in range(0,n):
    if(i==n-1):
        if(count>result):
            result=count
        break
    if(a[i+1]>a[i]):
        count+=1
    else:
        if(count>result):
            result=count
        count=1
print(result)