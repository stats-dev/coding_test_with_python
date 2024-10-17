# 입력
n = int(input())
# 번호
num = 0

arr1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(n): #열 단위 for loop
    i = n-i # curr col num
    if n % 2 == i % 2: ## 위로 올라가는 경우
        for j in range(n):
            j = n-j ## 행번호
            num += 1
            arr1[j-1][i-1] = num
    else:
        for k in range(n): # 내려가기
            num += 1
            arr1[k][i-1] = num ##k는 증가하는 행.
            
## 출력            
for r in arr1:
    for e in r:
        print(e, end = " ")
    print()