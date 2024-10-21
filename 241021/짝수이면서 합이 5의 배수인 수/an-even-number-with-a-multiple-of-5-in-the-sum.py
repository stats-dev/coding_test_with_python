# ## 3의 배수 5의 배수 숫자의 개수 세는 프로그램을 작성
# ## 함수
# def is_magic_num(n):
#     return n % 3 != 0 and n % 5 ==0


# cnt = 0

# for i in range(1, 101):
#     if is_magic_num(i):
#         cnt += 1

# print(cnt)

## 2자리 숫자에서 짝수이면서, 각 자리 수 합이 5의 배수 Yes, 아니면 No
def is_five(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())

print(is_five(n))