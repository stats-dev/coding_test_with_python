N = int(input())


arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)    
]

num = 1
for i in range(N):
    for j in range(N):
        if num < 10:
            arr_2d[i][j] = num
            num += 1
        else:
            num = 1
            arr_2d[i][j] = num
            num += 1

for r in arr_2d:
    for e in r:
        print(e, end= " ")
    print()