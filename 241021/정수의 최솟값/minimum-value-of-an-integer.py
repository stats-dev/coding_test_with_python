# def add(a, b, c=0):
#     return a + b + c

# print(add(1, 3))
a,b,c = tuple(map(int, input().split()))

def min_args(*args):
    return min(args)



print(min_args(a,b,c))