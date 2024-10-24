# N = int(input())


# def sum_even_odd(n):
#     if n == 0:
#         return n
#     if n == 1:
#         return 1
    
#     if n % 2 != 0:
#         return sum_even_odd(n - 2) + n
#     else:
#         return sum_even_odd(n - 2) + n

# print(sum_even_odd(N))

## 홀 짝이 같은 수의 합. 홀은 홀만, 짝은 짝만.

n = int(input())


# 1부터 n까지의 n과 홀짝이 같은 수들의 합을 반환합니다.
def get_num(n):
    if n <= 2:
        return n

    # n과 홀짝이 같은 수만을 재귀함수로 호출합니다.
    return get_num(n - 2) + n


print(get_num(n))