n = 5

arr_2d = [
    list(map(ord, input().split()))
    for _ in range(n)
]

for arr in arr_2d:
    for j in range(3):
        print(chr(arr[j]-32), end = ' ')
    print()