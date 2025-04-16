n, m = map(int, input().split())

mat1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

mat2 = [
    list(map(int, input().split())) 
    for _ in range(n)
    ]

newmat = [
    [1 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if mat1[i][j] == mat2[i][j]:
            newmat[i][j] = 0
        print(newmat[i][j], end=" ")
    print()


