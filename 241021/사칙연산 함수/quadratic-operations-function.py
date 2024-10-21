a, o, c = map(str, input().split())
result = 0

if o == '+':
    result = int(a) + int(c)
elif o == '-':
    result = int(a) + int(c)
elif o == '/':
    result = int(a) / int(c)
else:
    result = int(a) * int(c)

print(f"{a} {o} {c} = {result}")