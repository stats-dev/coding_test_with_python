n, m = map(int, input().split())


placed = [
    [0] * n
    for _ in range(n)
]



for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = r * c

for r in placed:
    for e in r:
        print(e, end = " ")
    print()