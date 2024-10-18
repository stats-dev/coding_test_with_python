n = int(input())

arr_2d = [
    [1] * i
    for i in range(1, n+1)
]

for i in range(1, n):
    for j in range(1,i):
        arr_2d[i][j] = arr_2d[i-1][j] + arr_2d[i-1][j-1]


for r in arr_2d:
    for e in r:
        print(e, end = " ")
    print()