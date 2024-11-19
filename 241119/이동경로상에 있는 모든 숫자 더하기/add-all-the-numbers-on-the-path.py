# n, t = tuple(map(int, input().split()))
# string = input()
# arr = [list(map(int, input().split())) for _ in range(n)]
# x, y = n//2, n//2
# total = arr[x][y]


# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# dir_num = 0

# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n
    
# for i in string:
#     if i == "R":
#         dir_num = (dir_num+1)%4
#     elif i == "L":
#         dir_num = (dir_num+3)%4
    
#     elif i == "F":
#         nx, ny = x + dx[dir_num], y + dy[dir_num]

#         if in_range(nx, ny):
#             total += arr[nx][ny]
#             x, y = nx, ny
#         else:
#             continue

# print(total)


n, t = tuple(map(int, input().split()))
commands = input()
board = [
    list(map(int, input().split()))
    for _ in range(n)
]


ans = 0


## 초기 시작 위치
x, y, move_dir = n // 2, n // 2, 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate():
    global ans
    global x, y, move_dir

    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    for command in commands:
        # R 명령 오른쪽
        if command == 'R':
            move_dir = (move_dir + 1) % 4
        # L 명령 왼쪽
        elif command == 'L':
            move_dir = (move_dir + 3) % 4
        ## 해당 방향 움직인다.
        else:
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            ## 이동 가능한 칸은 이동
            # 해당 칸의 숫자를 정답 ans에 계속 더한다.
            if in_range(nx, ny):
                ans += board[nx][ny]
                x = nx
                y = ny

ans += board[x][y]
simulate()

## 정답 출력
print(ans)
