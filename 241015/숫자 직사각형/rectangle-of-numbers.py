# n = 3

# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# num = 1
# for i in range(n):
#     for j in range(n):
#         arr_2d[i][j] = num
#         num += 2

# for row in arr_2d:
#     for e in row:
#         print(e, end= " ")
#     print()

a, b = map(int, input().split())

arr_2d = [
    [0 for _ in range(b)]
    for _ in range(a)
]

sum_val = 1
for i in range(a):
    for j in range(b):
        arr_2d[i][j] = sum_val
        print(arr_2d[i][j], end = " ")
        sum_val += 1
    print()