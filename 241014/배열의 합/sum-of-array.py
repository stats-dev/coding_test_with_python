arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

# 각 줄의 합
for i in range(4):
    print(sum(arr_2d[i]))