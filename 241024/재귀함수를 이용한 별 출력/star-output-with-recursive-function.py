n = int(input())

def print_star_tri(n):
    if n == 0:
        return
    print_star_tri(n-1)
    print('*' * n)


print_star_tri(n)