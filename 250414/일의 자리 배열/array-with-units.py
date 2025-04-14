a, b = map(int, input().split())

arr = [0 for _ in range(10)]

for i in range(2,10):
    arr[0] = a
    arr[1] = b
    arr[i] = (arr[i-2] + arr[i-1])%10

# arr.append(a+b)
# arr.append(a+b+b)
# arr.append(a+b+b+a+b)
for a in arr:
    print(a, end=' ')