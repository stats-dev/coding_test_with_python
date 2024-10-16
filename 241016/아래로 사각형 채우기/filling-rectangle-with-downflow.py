n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]


num = 1
for i in range(n):
    for j in range(n):
        arr_2d[j][i] = num
        num += 1


for r in arr_2d:
    for e in r:
        print(e, end = " ")
    print()