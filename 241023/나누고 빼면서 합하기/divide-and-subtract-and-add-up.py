n, m = tuple(map(int, input().split()))

A = list(map(int, input().split()))
sum = 0

def sum_vals(m):
    global sum
    while m > 1:
        sum += A[m]
        if m % 2 == 0:
            m //= 2
            sum += A[m]
        else:
            m -= 1
            sum += A[m]
    return sum

print(sum_vals(m))