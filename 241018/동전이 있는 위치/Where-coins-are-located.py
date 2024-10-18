# a, b = 1, 3

# placed = [
#     [0 for _ in range(11)]
#     for _ in range(11)
# ]


# for _ in range(10):
#     r, c = tuple(map(int, input().split()))
#     placed[r][c] = 1

# exists = True if placed[a][b] == 1 else False
# print(exists)

n, m = map(int, input().split())

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = 1

for r in placed:
    for e in r:
        print(e, end=" ")
    print()