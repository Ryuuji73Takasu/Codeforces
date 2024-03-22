n = int(input())

cost = [0] * 100000 
maxx = 0  

for _ in range(n):
    x = int(input())
    cost[x] += 1
    maxx = max(maxx, x)

for i in range(1, maxx + 1):
    cost[i] += cost[i - 1]


q = int(input())


for _ in range(q):
    m = int(input())
    if m >= maxx:
        print(n)
    else:
        print(cost[m])