## n, m
n, m = map(int, input().split())

arr2d = [
    [0] * n
    for _ in range(n)
]

cnt = 1
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr2d[r-1][c-1] = cnt
    cnt += 1

for i in range(n):
    for j in range(n):
        print(arr2d[i][j], end = " ")
    print()