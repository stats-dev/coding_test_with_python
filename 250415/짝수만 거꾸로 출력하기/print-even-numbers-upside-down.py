n = int(input())

lst = list(map(int, input().split()))

for i in range(n):
    if lst[n-i-1] % 2 == 0:
        print(lst[n-i-1], end=' ')
