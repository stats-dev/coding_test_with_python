N = int(input())

arr = tuple(map(int, input().split()))

def is_abs(a):
    if a < 0:
        a = -a
    print(a, end=" ")

for a in arr:
    is_abs(a)