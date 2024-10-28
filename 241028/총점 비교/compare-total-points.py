## from functools import cmp_to_key

## tuple로 풀이

n = int(input())

scores = [
    list(tuple(input().split()))
    for _ in range(n)
]

scores.sort(key = lambda x : (int(x[1]) + int(x[2]) + int(x[3])))

for score in scores:
    name, kor, eng, math = score
    print(name, kor, eng, math)