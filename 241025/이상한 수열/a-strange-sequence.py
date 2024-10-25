N = int(input())

def abnor_seq(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return abnor_seq(n // 3) + abnor_seq(n - 1)

print(abnor_seq(N))