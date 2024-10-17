n = int(input())

arr1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]


num = 1
for i in range(n):
    for j in range(n):
        if n-j-1 > 0: 
            arr1[n-j-1][n-i-1] = num
            num += 1
        else:
            arr1[n-j-1][n-i-1] = num
            

for r in arr1:
    for e in r:
        print(e, end = " ")
    print()