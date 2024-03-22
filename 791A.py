a,b = map(int, input().split())
aa= a*3
bb= b*2
for i in range (1,b+1):
    if(aa>bb):
        print(i)
        break
    aa=aa*3
    bb=bb*2