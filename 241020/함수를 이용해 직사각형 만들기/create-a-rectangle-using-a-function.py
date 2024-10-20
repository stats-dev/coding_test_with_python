# def print_nm(n, m):
#     for _ in range(n):
#         print("*" * m)


def print_nm(n, m):
    for _ in range(n):
        print("1" * m)


n, m = tuple(map(int, input().split()))

print_nm(2, 3)