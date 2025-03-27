a = input()

# Please write your code here.
max_n = 0

# a : 0과 1로 이루어진 수

for i in range(len(a)):
    flipped_bit = '0' if a[i] == '1' else '1'

    # 새로운 이진 문자열 생성
    new_binary = a[:i] + flipped_bit + a[i+1:]

    # 이진 문자열을 정수로 변환합니다.
    n = int(new_binary, 2)

    # 최댓값
    max_n = max(max_n, n)

print(max_n)