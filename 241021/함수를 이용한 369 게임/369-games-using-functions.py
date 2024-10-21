## 3의 배수 아니다.
## 각 자리 숫자가 다른 경우만

# def all_diff(n):
#     return (n // 10) != (n % 10)

# def is_ma_num(n):
#     return n % 3 !=0 and all_diff(n) ## return 값이 true

# cnt = 0
# for i in range(10, 100): ## 두자리 수
#     if is_ma_num(i):
#         cnt += 1

# print(cnt)

a, b = tuple(map(int, input().split()))

## a <= x <= b 3,6,9 하나 or 숫자가 3배수


def is_threes(n):
    threes = [3, 6, 9]
    while n > 0:
        if n % 10 in threes:
            return True
        n //= 10 ## 계속 나눠줘야 겨우 도달할 수 있구만.

def is_sam(n):
    return (n % 3 == 0)

cnt = 0

for i in range(a, b+1):
    if is_threes(i) or is_sam(i):
        cnt += 1

print(cnt)