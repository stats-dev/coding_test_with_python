# def f(n):
#     # 종료 조건
#     if n == 1:
#         return 2
#     if n == 2:
#         return 7
    

#     return f(n - 1) + 2 * f(n - 2)


# print(f(4))

N = int(input())

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return f(n - 1) + f (n - 2)

print(f(N))