n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]


num = 0
for i in range(m):
    for j in range(n):
        if i % 2 != 0:
            arr_2d[n-1-j][i] = num 
        else:
            arr_2d[j][i] = num
        num += 1



for r in arr_2d:
    for e in r:
        print(e, end = " ")
    print()