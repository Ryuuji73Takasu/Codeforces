s=str(input())
n=len(s)
st=""
i=0
while i < n:
    if(i>=(n-1)):
        if(i==n-1):
            st+="0"
        break
    elif (s[i]=='-'):
        if(s[i+1]=='.'):
            i+=1
            st+="1"
        elif(s[i+1]=='-'):
            i+=1
            st+="2"
    else:
        st+="0"
    i+=1

print(st)