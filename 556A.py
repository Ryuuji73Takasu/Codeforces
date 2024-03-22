n = int(input())
s = str(input())
z=0
o=0
for i in range(0,n):
    if(s[i]=="0"):
        z+=1
    else:
        o+=1
print(abs(z-o)) 