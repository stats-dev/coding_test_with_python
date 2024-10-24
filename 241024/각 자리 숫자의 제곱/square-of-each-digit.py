N = int(input())

def sum_digits_square(N):
    if N < 10:
        return N**2
    
    return sum_digits_square(N // 10) + (N % 10)**2

print(sum_digits_square(N))