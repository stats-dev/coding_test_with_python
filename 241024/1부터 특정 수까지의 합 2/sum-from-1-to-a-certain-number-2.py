# def fact(n):
#     if n == 1:
#         return 1

#     return fact(n - 1) * n
# 정수 N
N = int(input())

def totalsum(N):
    if N == 1:
        return 1
    
    return totalsum(N - 1) + N

print(totalsum(N))