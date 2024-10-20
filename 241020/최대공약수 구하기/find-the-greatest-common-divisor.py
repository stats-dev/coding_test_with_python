n, m = tuple(map(int, input().split()))


def gcd(n, m):
    num = 0
    if n >= m:
        for i in range(1, n):
            if n % i == 0 | m % i == 0:
                num = i
    else:
        for j in range(1, m):
            if n % j == 0 | m % j == 0:
                num = j
    print(num)

gcd(n, m)