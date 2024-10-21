# def add(a, b, c=0):
#     return a + b + c

# print(add(1, 3))

def min_args(*args):
    return min(args)

numbers = tuple(map(int, input().split()))

print(min(numbers))