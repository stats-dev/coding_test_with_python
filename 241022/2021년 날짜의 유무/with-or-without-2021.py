M, D = map(int, input().split())

def is_month(m, d):
    while m > 0 and m < 13:
        if m == 2 and d < 29:
            return True
        elif m % 2 == 0:
            return d < 32
        else:
            return d < 31
        return False

if is_month(M, D):
    print("Yes")
else:
    print("No")