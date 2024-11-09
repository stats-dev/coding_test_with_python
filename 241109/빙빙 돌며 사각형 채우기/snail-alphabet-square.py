n, m = tuple(map(int, input().split()))


arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0 ## 시작이 0,0일때, 오른쪽부터 간다.

arr[x][y] = 1


# for i in range(2, (n * m) + 1):
#     nx, ny = x + dxs[dir_num], y + dys[dir_num]

#     if in_range(nx, ny) and arr[nx][ny] == 0:
#         x, y = nx, ny
#         arr[x][y] = i

#     else:
#         dir_num = (dir_num + 1) % 4 ## 시계방향 이동


for i in range(2, (n * m) + 1):

    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:

        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]

    arr[x][y] = i

# for row in arr:
#     for ele in row:
#         print(chr(ele + ord('A') - 1), end=' ')
#     print()

for i in range(n):
    for j in range(m):
        if arr[i][j] > 26:
            arr[i][j] %= 26
        print(chr(arr[i][j] + ord('A') - 1), end = " ")
    print()