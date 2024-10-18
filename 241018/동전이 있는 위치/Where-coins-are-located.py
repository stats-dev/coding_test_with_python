n, m = map(int, input().split())

## 각 값이 좌표값.

## 0으로 배치
arr2d = [
    [0] * n
    for _ in range(n)
]

## 입력값을 받고, 각 값을 좌표로 저장.
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr2d[r-1][c-1] = 1

for r in arr2d:
    for e in r:
        print(e, end=" ")
    print()