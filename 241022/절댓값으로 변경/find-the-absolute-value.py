# N = int(input())

# arr = tuple(map(int, input().split()))

# def is_abs(a):
#     if a < 0:
#         a = -a
#     print(a, end=" ")

# for a in arr:
#     is_abs(a)

## 리스트는 mmutable 하다.
n = int(input())
arr = list(map(int, input().split()))

def abs_val(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]
    
    return

abs_val(arr)

for e in arr:
    print(e, end=" ")