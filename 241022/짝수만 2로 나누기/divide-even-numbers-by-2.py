# def even_only_div(lst):
#     result = []
#     for i in lst:
#         if i % 2 == 0:
#             result.append(i // 2)
#         else:
#             result.append(i)
#     return result

# N = int(input())
# ns = map(int, input().split())

# ans = even_only_div(ns)

# for i in ans:
#     print(i, end = " ")

# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))


def modify(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2


modify(arr)
for elem in arr:
    print(elem, end=" ")