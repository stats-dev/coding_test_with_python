# def add(a, b, c=0):
#     return a + b + c

# print(add(1, 3))
a,b,c = tuple(map(int, input().split()))

def min_args(*args):
    return min(args)



# print(min_args(a,b,c))

## 정석
def get_min(a,b,c):
    min_val = a
    if min_val > b:
        min_val = b
    if min_val > c:
        min_val = c
    
    return min_val

print(get_min(a,b,c))