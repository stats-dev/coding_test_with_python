n = int(input())

strs = [input() for _ in range(n)]


strs.sort()

for e in strs:
    print(e)