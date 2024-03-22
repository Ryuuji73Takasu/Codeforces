r,c = map(int,input().split())
mat = []

for _ in range(r):
    rows = input().strip()
    mat.append(rows)

for i in range(r):
        mat[i] = list(mat[i])

print(mat)



# 5 5
# ..S..
# ****.
# T....
# ****.
# .....
