arr_2d1 = [
    list(map(int, input().split()))
    for _ in range(4)
]

arr_2d2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_mul = [
    [0 for _ in range(3)]
    for _ in range(3)
]


for i in range(3):
    for j in range(3):
        arr_mul[i][j] = arr_2d1[i][j] * arr_2d2[i][j]
        print(arr_mul[i][j], end = " ")
    print()