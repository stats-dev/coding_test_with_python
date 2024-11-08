n, m = map(int, input().split())


arr = [ 
    [0 for _ in range(m)]
    for _ in range(n)
]


x, y = 0, 0

dir_num = 1

arr[x][y] = 1


dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0] 

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(2, n * m + 1):
    while True:
        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]

        if in_range(nx, ny) and arr[nx][ny] == 0:
            x = nx
            y = ny
            arr[nx][ny] = i
            break
        else:
            dir_num = (dir_num + 3) % 4

for row in arr:
    for ele in row:
        print(ele, end=" ")
    print()
        



def move(dir_num):
    nx = x + dxs[dir_num]


# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n


# ### x y 시작 후 next_dir 방향 이동 후 위치 반환
# def move(x, y, next_dir):
#     dxs, dys = [1,0,-1,0], [0,-1,0,1]
#     nx, ny = x + dxs[next_dir], y + dys[next_dir]
#     return nx, ny, next_dir

# def simulate(x, y, move_dir):
#     move_num = 0

#     while in_range(x, y):
#         ## 0 <-> 1, 2 <-> 3: XOR 연
#         if arr[x][y] == '/':
#             x, y, move_dir = move(x, y, move_dir ^ 1)
#         ## 0 <-> 3 / 1 <-> 2
#         else:
#             x, y, move_dir = move(x, y, 3 - move_dir)
        
#         move_num += 1

#     return move_num