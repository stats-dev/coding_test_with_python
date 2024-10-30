# dir_num = 3
# x, y = 1, 5
# dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# if dir_num == 0:
#     dir_num = 2 ## 0 -> 2
# elif dir_num == 1:
#     dir_num = 3
# elif dir_num == 2:
#     dir_num = 1
# else:
#     dir_num = 0


# ## move
# nx, ny = x + dx[dir_num], y + dy[dir_num]

## N 북 먼저 : 상 우 하 좌 인데, 왼쪽 가면 시계방향으로 -> 상 좌 하 우 반시계
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cmd = list(input())
x, y = 0, 0
dn = 0

for c in cmd:
    if c == 'L':
        dn = (dn + 3) % 4 ##왼쪽 이동 -1 = +3 (총 4가지)
    elif c == 'R':
        dn = (dn + 1) % 4 ## 우측 이동 +1
    else: ## c F라면 이동
        x += dx[dn]
        y += dy[dn]

print(x, y)