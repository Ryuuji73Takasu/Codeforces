n, k = map(int,input().split())
flag= 1
for i in range(0,n):
    for j in range(0,k):
        if (i%2==0):
            print("#",end="")
        if (flag==1):
            if (i%2==1 and j!=k-1):
                print(".",end="")
            if (i%2==1 and j==k-1):
                print("#",end="")
                flag=-1
                break
        if (flag==-1):
            if (i%2==1 and j==0):
                print("#",end="")
            if (i%2==1 and j>0):
                print(".",end="")
            if (i%2==1 and j==k-1):
                flag=1
                break
    print("")
        
