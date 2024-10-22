n1, n2 = tuple(map(int, input().split()))

A = list(tuple(map(int, input().split())))
B = list(tuple(map(int, input().split())))

# def is_continuous_subsequence(sub, main):
#     return any(main[i:i + len(sub)] == sub for i in range(len(main) - len(sub) + 1))

# if is_continuous_subsequence(B, A):
#     print("Yes")
# else:
#     print("No")

## n to n2 까지 인덱스 값에서 동일 배열 확인
def is_same(n):
    for i in range(n2):
        if A[i+n] != B[i]:
            return False ## 하나라도 틀리면 안됨.
    return True


def is_seq():
    for i in range(n1 - n2 + 1):
        if is_same(i):
            return True
    return False

if is_seq():
    print("Yes")
else:
    print("No")

# def is_seq(arr1, arr2):
#     for i in range(len(arr1) - len(arr2) + 1):
#         if arr1[i:i + len(arr2)] == arr2[i]:
#             return True
#         return False

# print(is_seq(arr1, arr2))