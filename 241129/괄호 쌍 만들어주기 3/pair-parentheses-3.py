# blank = list(input()) ## 빈칸 필요한데,

# answer = 0

# for i in range(len(blank)):
#     for j in blank[i:]:
#         if blank[i]+j=='()':
#             answer += 1

# print(answer)

## 간단 해결법, 일일이 잡아보면, 순서대로 문자 확인 ()

string = input()
n = len(string)

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if string[i] == '(' and string[j] == ')':
            cnt += 1

print(cnt)