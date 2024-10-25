n = int(input())
lst = list(map(int, input().split()))

## 홀수 번째 원소마다, 입력값의 중앙값 출력

odd_lst = []

for idx in range(n):
    if idx % 2 == 0:
        odd_lst.append(lst[idx // 2])

for e in odd_lst:
    print(e, end = " ")