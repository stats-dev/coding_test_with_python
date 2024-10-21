a, o, c = map(str, input().split())
result = 0

if o == '+':
    result = int(a) + int(c)
    print(f"{a} {o} {c} = {result}")
elif o == '-':
    result = int(a) - int(c)
    print(f"{a} {o} {c} = {result}")
elif o == '/':
    result = int(a) // int(c)
    print(f"{a} {o} {c} = {result}")
elif o == '*':
    result = int(a) * int(c)
    print(f"{a} {o} {c} = {result}")
else:
    print(False)