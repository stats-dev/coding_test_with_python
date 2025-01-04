n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
max_cnt = 0

for i in range(n):
    for j in range(n - 1):
        for k in range(n - 2):
            max_cnt = max(max_cnt, grid[i][j] + grid[i][j + 1] + grid[i][k + 2])

print(max_cnt)

# n = 5
# arr = [[1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [0, 1, 1, 0, 1],
#        [0, 0, 0, 1, 0],
#        [0, 0, 0, 0, 0]]

# max_cnt = 0
# for i in range(n):
#     for j in range(n - 1):
#         max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1])

# print(max_cnt)