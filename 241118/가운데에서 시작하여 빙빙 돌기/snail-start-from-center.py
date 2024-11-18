# n = int(input())

# arr = [
#     [0] * n
#     for _ in range(n)
# ]


# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n

# dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]

# cur_dir = 0

# x, y = n-1, n-1

# arr[x][y] = n ** 2

# for i in range(n ** 2 - 1, 0, -1) : 
#     nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
#     if not in_range(nx, ny) or arr[nx][ny] > 0:
#         cur_dir = (cur_dir + 1) % 4
    
#     x, y = x + dxs[cur_dir], y + dys[cur_dir]
#     arr[x][y] = i

# for row in arr :
#     for elem in row:
#         print(elem, end = " ")
#     print()

### 안에서 밖으로?

n = int(input())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

## 시작 위치 방향, 이동 횟수 2로 나눈 값이 정중앙 가정. 처음이 1번 이동
curr_x, curr_y = n // 2, n // 2
move_dir, move_num = 0, 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < not

def move():
    global curr_x, curr_y


    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

def end():
    return not in_range(curr_x, curr_y)

cnt = 1

while not end():
    ## move_num 만큼 이동
    for _ in range(move_num):
        grid[curr_x][curr_y] = cnt
        cnt += 1

        move()

        ## 이동 도중 격자 벗어나면, 움직이는 것 종료
        if end():
            break
    
    move_dir = (move_dir + 1) % 4

    # 현재 왼, 오른 경우에 특정 방향 움직 횟수 1증가
    if move_dir == 0 or move_dir == 2:
        move_num += 1
    

## 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()



