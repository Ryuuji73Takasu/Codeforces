t = int(input())
for i in range(0,t):
    n = int(input())
    string = str(input())
    flag=0
    for j in range(0,n,3):
        if(j+2>n-1):
            if(j+1>n-1):
                flag=1
            else:
                flag=0
            break
        if(string[j+1]==string[j+2]):
                flag=1
        else:
            flag=0
            break
    if(flag==1):
        print("YES")
    elif(flag==0):
        print("NO")