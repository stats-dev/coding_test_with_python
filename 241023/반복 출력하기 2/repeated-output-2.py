n = int(input())

def print_helw(n):
    if n == 0:
        return
    print_helw(n-1)
    print("HelloWorld")

print_helw(n)