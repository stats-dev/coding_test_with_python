arr = [['book', 3000],['mask',1000]]

n = int(input())

if n >= arr[0][1]:
    print(arr[0][0])
elif n >= arr[1][1]:
    print(arr[1][0])
else:
    print('no')