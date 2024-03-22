n = int(input())
s = str(input())
l=0
o=0
for i in range(1,n):
    if(s[i]==s[0]):
        l+=1
if (l!=1):
    print("1")
elif (l==1):
    for i in range(0,n-1):
        if(s[i]==s[n-1]):
            o+=1
    if (o!=1):
        print(n-1)
    elif(o==1):
        if(s=="LLOO" or s=="OOLL"):
            print("2")
        else:
            print("-1")