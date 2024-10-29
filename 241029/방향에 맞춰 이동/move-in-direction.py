# num = 2
# x, y = 1, 5
# dx, dy = [1,0,-1,0], [0,-1,0,1]

# nx, ny = x + dx[num], y + dy[num]

# n = int(input())


x, y = 0, 0

# dx, dy = [1,0,-1,0], [0,-1,0,1]

# E, S, W, N = 0, 1, 2, 3


# for _ in range(n):
#     arr = input().split()
#     dr, dt = arr[0], int(arr[1])

#     if dr=='N':
#         d_num=3

#     elif dr=='E':
#         d_num=0

#     elif dr=='S':
#         d_num=1

#     else:
#         d_num=2

    
#     x,y=x+dt*dx[d_num],y+dt*dy[d_num]

# print(x, y)

# nx = x + dx[move_dir] * dist
# ny = y + dy[move_dir] * dist

n = int(input())
x, y = 0, 0

## 동 서 남북이라면,
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

## move
for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist) ## 정수화

    # 각 방향에 맞게 번호 생성, e, w, s, n 0, 1, 2, 3
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3
    

    ## dist move pos
    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)