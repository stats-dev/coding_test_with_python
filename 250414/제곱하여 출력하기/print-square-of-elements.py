n = int(input())
nums = list(map(int, input().split()))

pownum = [x**2 for x in nums]

for p in pownum:
    print(p, end=' ')