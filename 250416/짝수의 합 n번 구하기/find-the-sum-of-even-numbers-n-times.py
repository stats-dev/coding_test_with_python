n = int(input())

# total = 0

for _ in range(n):
    total = 0
    a, b = map(int, input().split())
    for i in range(a,b + 1):
        if i % 2 == 0:
            total += i
    print(total)