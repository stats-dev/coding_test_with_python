n = int(input())
lst = list(map(int, input().split()))


lst.sort()

max_val = 0

for i in range(n):

    sum = lst[i] + lst[2 * n - i - 1]
    if sum > max_val:
        max_val = sum

print(max_val)