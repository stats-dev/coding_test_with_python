n1 = list(input())
n2 = list(input())

n1.sort()
n2.sort()

if len(n1) == len(n2):
    if n1 == n2:
        print("Yes")
    else:
        print("No")
else:
    print("No")