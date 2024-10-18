n = int(input())


arr1 = [
    [1] * n
    for _ in range(n)
]

for i in range(1, n):
    for j in range(1, n):
        arr1[i][j] = arr1[i-1][j-1] + arr1[i-1][j] + arr1[i][j-1]


for r in arr1:
    for e in r:
        print(e, end = " ")
    print()