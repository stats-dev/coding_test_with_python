a, b = map(int, input().split())

def min_args(a, b):
    n1 = min(a, b) * 2
    n2 = max(a, b) + 25
    return n1, n2


result = min_args(a,b)

for r in result:
    print(r, end=" ")