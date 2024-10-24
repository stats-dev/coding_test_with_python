n = int(input())


def print_star_rec(n):
    if n < 1:
        return
    print("* " * n)
    print_star_rec(n-1)
    print("* " * n)


print_star_rec(n)