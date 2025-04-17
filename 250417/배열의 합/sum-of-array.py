

## 4개의 행렬을 2차원으로 입력받기
arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

for a in arr:
    print(sum(a))