n = int(input())


arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(n):
    for j in range(n):
        if i % 2 != 0:
            arr[j][i] = n - j
        else:
            arr[j][i] = j + 1
        
for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()