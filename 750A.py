a, b = map(int,input().split(" ",2))
summ = 0
for i in range (1,a+1):
    summ = summ + (5*i)
    if (summ> 240-b):
        print(i-1)
        break
    if (i==a):
        print(i)