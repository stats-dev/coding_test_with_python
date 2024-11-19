n, t = tuple(map(int, input().split()))
string = input()
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = n//2, n//2
total = arr[x][y]


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

dir_num = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    
for i in string:
    if i == "R":
        dir_num = (dir_num+1)%4
    elif i == "L":
        dir_num = (dir_num+3)%4
    
    elif i == "F":
        nx, ny = x + dx[dir_num], y + dy[dir_num]

        if in_range(nx, ny):
            total += arr[nx][ny]
            x, y = nx, ny
        else:
            continue

print(total)
