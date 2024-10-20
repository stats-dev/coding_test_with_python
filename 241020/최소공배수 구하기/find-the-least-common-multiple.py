n, m = tuple(map(int, input().split()))


num = 0
ln = 0
lm = 0
result = 0
## 최소 공배수 : 최대공약수 나눈 몫 6 * 2 * 3 = 36 곱하기
def lcd(n,m):
    if n >= m:
        for i in range(1, n):
            if n % i == 0 | m % i == 0:
                num = i
    else:
        for j in range(1, m):
            if m % j == 0 | n % j == 0:
                num = j
    
    ln = n // num
    lm = m // num
    result = num * ln * lm
    print(result)

lcd(n, m)