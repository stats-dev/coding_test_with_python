n, m = map(int, input().strip().split())

arr1 = [
    list(map(int, input().split()))
    for _ in range(n)
]


arr2 = [
    list(map(int, input().split()))
    for _ in range(n)
]


arr_diff = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if arr1[i][j] != arr2[i][j]:
            arr_diff[i][j] += 1

for r in arr_diff:
    for e in r:
        print(e, end = " ")
    print()