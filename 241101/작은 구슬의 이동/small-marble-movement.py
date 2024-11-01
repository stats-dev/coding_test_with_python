n, t = tuple(map(int, input().split()))

r, c, d = input().split()


# 각 알파벳 별 방향 번호를 설정합니다.
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

r, c, mdir = int(r) - 1, int(c) - 1, mapper[d]



dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]
## 북 동 남 서

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for _ in range(t):
    nx, ny = r + dxs[mdir], c + dys[mdir]

    if in_range(nx, ny):
        r, c = nx, ny
    ##벽
    else:
        mdir = 3 - mdir

print(r + 1, c + 1)

# if d == 'R':
#     for _ in range(t):
#         nx = r + dxs[mdir]
#         ny = c + dys[mdir]
#         if in_range(nx, ny):
#             r = nx
#             c = ny
#         else:
#             mdir = 3 - mdir


# elif d == 'D':
#     mdir = 1
#     for _ in range(t):
#         nx = r + dxs[mdir]
#         ny = c + dys[mdir]
#         if in_range(nx, ny):
#             r = nx
#             c = ny
#         else:
#             mdir = 3 - mdir

# elif d == 'L':
#     mdir = 2
#     for _ in range(t):
#         nx = r + dxs[mdir]
#         ny = c + dys[mdir]
#         if in_range(nx, ny):
#             r = nx
#             c = ny
#         else:
#             mdir = 3 - mdir

# else:
#     mdir = 3
#     for _ in range(t):
#         nx = r + dxs[mdir]
#         ny = c + dys[mdir]
#         if in_range(nx, ny):
#             r = nx
#             c = ny
#         else:
#             mdir = 3 - mdir

# print(r+1, c+1)