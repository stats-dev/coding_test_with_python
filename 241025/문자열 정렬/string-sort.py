## 문자열 정렬은 sort 못씁니다.

strs = input()


str_lst = list(strs)
str_lst.sort()
str_lst = ''.join(str_lst)
print(str_lst)