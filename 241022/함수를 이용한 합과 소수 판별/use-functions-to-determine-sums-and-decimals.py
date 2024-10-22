a, b = tuple(map(int, input().split()))


def is_prime(n):
    cnt = 0
    for i in range(2, n):
        if n % i != 0:
            return True
    return cnt == 0
    

def is_even_sum(n):
    while n > 10 and n < 100:
        if ((n // 10) + (n % 10)) % 2 == 0:
            return True
        return False

cnt = 0
for i in range(a, b + 1):
    if is_prime(i) and is_even_sum(i):
        cnt += 1
        print(i)

print(cnt)