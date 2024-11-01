n = int(input())

# dlists = [
#     list(input().split())
#     for _ in range(n)
# ]

# print(dlists)
## dictionary

dirs = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

x, y, d_num = 0, 0, 0
dxs, dyx = [-1, 0, 1, 0], [0, 1, 0, -1]

cnt = 0

for i in range(n):
    d, f = input().split()
    d_num = dirs[d]

    for j in range(int(f)):
        x, y = x + dxs[d_num], y + dyx[d_num]
        cnt += 1 ## 시간 카운트
        if x == 0 and y == 0:
            print(cnt)
            exit(0)

if x != 0 and y != 0:
    print(-1)