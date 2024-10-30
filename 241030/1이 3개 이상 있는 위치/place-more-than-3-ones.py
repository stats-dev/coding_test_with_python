# x, y = 2, 1
# dx, dy = [0, 1,0,-1], [1,0,-1,0] ## 상 우 하 좌

# cnt = 0

# for dir_num in range(4):
#     nx, ny = x + dx[dir_num], y + dy[dir_num]
#     if a[nx][ny] == 1:
#         cnt += 1

# print(cnt)


n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

xys = [(x, y) for x, row in enumerate(arr) for y, val in enumerate(row) if val == 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

total = 0
cnt = 0
for x, y in xys:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt >= 3:
        total += 1

print(total)