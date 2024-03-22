n = int(input())
ls = [int(x) for x in input().split()]

matchls = []
flag=0

for j in range(0,n):
    for i in range(0,n):
        if (i%2==0):
            if(ls[i]==n-1):
                ls[i]=0
            else:
                ls[i]=ls[i]+1
        elif (i%2==1):
            if(ls[i]==0):
                ls[i]=n-1
            else:
                ls[i]=ls[i]-1
        if (flag==0):
            matchls.append(i)
            if(i==n-1):
                flag=1
        
    if(matchls==ls):
        print("Yes")
        flag=2
        break
if (flag==1):
    print("No")