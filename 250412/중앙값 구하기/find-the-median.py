# a,b,c = map(int, input().split())

# if a > c:
#     if a > b:
#         if b > c:
#             print(b)
#         else:
#             print(c)
#     else:
#         print(a)
# else:
#     print(a)

## list
arr = list(map(int, input().split()))
arr.sort()

print(arr[1])
