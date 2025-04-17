n = int(input())


arr = [
    [0 for _ in range(n)]
    for _ in range(n)
    ]


cnt = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            arr[i][j] = j + 1
    else:
        for j in range(n):
            arr[i][j] = n - j

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
    
        
