def even_only_div(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i // 2)
        else:
            result.append(i)
    return result

N = int(input())
ns = map(int, input().split())

ans = even_only_div(ns)

for i in ans:
    print(i, end = " ")