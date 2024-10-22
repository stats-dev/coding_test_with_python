a = input()

def is_same(a):
    cnt = 0
    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            cnt += 1
    return cnt

if is_same(a) > 2:
    print("Yes")
else:
    print("No")