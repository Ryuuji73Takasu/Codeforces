t = int(input())

def operation(prv, cur, nxt):
    prv = prv - 1
    cur = cur - 2
    nxt = nxt - 1
    return prv, cur, nxt
    
for _ in range(t):    

    n = int(input())
    lst=[]
    flag=0
    lst = list(map(int, input().split()))

    for i in range(0,n-1):
        if i == n-2:
            if lst[i]!=0 or lst[i+1]!=0:
                flag=1
            break

        if lst[i]<0 or lst[i+2]<0 or lst[i+1]<0:
            flag=1
            break

        lst[i+1]= lst[i+1]-lst[i]*2
        lst[i+2]=lst[i+2]-lst[i]
        lst[i]=0


    if flag==0:
        print("YES")
    elif flag==1:
        print("NO")