n, m = tuple(map(int, input().split()))

A = [0] + list(map(int, input().split()))
# sum = 0

# def sum_vals(m):
#     global sum
#     while m > 0:
#         sum += A[m]
#         if m % 2 == 0:
#             m //= 2
#         else:
#             m -= 1
#     return sum

# print(sum_vals(m))

def get_answer():
    global m
    
    return_val = 0
    while m:
        return_val += A[m]

        if m%2 == 0:
            m //= 2
        else:
            m -= 1
    
    return return_val

print(get_answer())