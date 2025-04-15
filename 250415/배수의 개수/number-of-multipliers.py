
arr = [int(input()) for _ in range(10)]

cnt1, cnt2 = 0, 0

for num in arr:
    if num % 3 == 0:
        cnt1 += 1
    
    if num % 5 == 0:
        cnt2 += 1

print(cnt1, cnt2)
