a, b = tuple(map(int, input().split()))

def is_fn(a, b):
    if a > b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    return a,b

a,b = is_fn(a,b)

print(a,b)