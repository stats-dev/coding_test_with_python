

mat = []

for _ in range(3):
    row = list(map(int, input().split()))
    mat.append(row)


for i in range(3):
    for j in range(3):
        print(mat[i][j] * 3, end=" ")
    print()
