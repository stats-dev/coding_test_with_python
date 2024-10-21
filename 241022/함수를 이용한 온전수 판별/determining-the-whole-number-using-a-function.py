a, b = tuple(map(int, input().split()))


def is_onjeonsu(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True
    # return n % 2 != 0 and n % 10 != 5 and ~(n % 3 == 0 and n % 9 != 0)


cnt = 0
for i in range(a, b+1):
    if is_onjeonsu(i):
        cnt += 1
        

print(cnt)