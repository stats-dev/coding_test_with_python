a, b, c = map(int,input().split())


def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

def multi_digits(a, b, c):
    result = a * b * c
    return sum_digits(result)

print(multi_digits(a,b,c))