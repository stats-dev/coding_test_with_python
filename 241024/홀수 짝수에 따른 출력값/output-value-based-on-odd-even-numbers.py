N = int(input())


def sum_even_odd(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    
    if n % 2 != 0:
        return sum_even_odd(n - 2) + n
    else:
        return sum_even_odd(n - 2) + n

print(sum_even_odd(N))