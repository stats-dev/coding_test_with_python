n, m = map(int, input().split())

# arr_2d = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]


# # num = 1
# # for i in range(n):
# #     for j in range(m):
# #         if j <= m:
# #             arr_2d[j][i-j] = num
# #             num += 1
# #         else: 
# #             arr_2d[j-i][j] = num

def diagonal_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1
    for diag in range(n + m - 1):
        if diag < m:
            row, col = 0, diag
        else:
            row, col = diag - m + 1, m - 1
        while row < n and col >= 0:
            matrix[row][col] = num
            num += 1
            row += 1
            col -= 1
    return matrix

result = diagonal_matrix(n, m)

for r in result:
    for e in r:
        print(e, end = " ")
    print()