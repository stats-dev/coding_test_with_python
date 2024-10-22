a, b = map(int, input().split())

def min_args(a, b):
    if a > b:
        a = a + 25
        b = b * 2
    else:
        b = b + 25
        a = a * 2
    return a, b


result = min_args(a,b)

for r in result:
    print(r, end=" ")