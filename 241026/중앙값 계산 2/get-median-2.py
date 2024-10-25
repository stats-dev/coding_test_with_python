n = int(input())
lst = list(map(int, input().split()))

## 홀수 번째 원소마다, 입력값의 중앙값 출력

odd_lst = []

for idx in range(1, n+1, 2):
    lst1 = lst[:idx]
    lst1.sort()
    odd_lst.append(lst1[idx // 2])
    # print(odd_lst)

for e in odd_lst:
    print(e, end = " ")