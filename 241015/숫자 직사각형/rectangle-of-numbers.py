n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

sum_v = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = sum_v
        sum_v += 1

for row in arr:
    for ele in row:
        print(ele, end = " ")
    print()