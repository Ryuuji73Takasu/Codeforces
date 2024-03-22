t = int(input())
for i in range(0,t):
    n = int(input())
    s = list(input())
    f = list(input())
    count01 = 0
    count10 = 0

    for i in range(0,n):
        if(s[i]=="0" and f[i]=="1"):
            count01+=1
        elif(s[i]=="1" and f[i]=="0"):
            count10+=1
    print(max(count01,count10))  