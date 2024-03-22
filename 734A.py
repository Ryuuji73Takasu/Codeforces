n= int(input())
string = str(input())
if(string.count("D")>string.count("A")):
    print("Danik")
elif(string.count("D")<string.count("A")):
    print("Anton")
else:
    print("Friendship")