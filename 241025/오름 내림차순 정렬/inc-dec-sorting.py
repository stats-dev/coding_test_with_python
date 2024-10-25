## n 숫자 오름차순 정렬?


n = int(input())

lst = list(map(int, input().split()))

lst.sort()
## 첫째는 오름차순
for e in lst:
    print(e, end=" ")

print()

for e in lst[::-1]:
    print(e, end=" ")