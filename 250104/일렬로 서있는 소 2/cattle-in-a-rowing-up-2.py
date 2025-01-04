from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))


L = [0 for _ in range(n)]
for i in range(n):
    tmp = 0
    for j in range(i):
        if base[j] <= base[i]:
            tmp += 1
    L[i] = tmp

R = [0 for _ in range(n)]
for i in range(n-1,-1,-1):
    tmp = 0
    for j in range(i+1, n):
        # print(i,j,base[i], base[j])
        if base[j] >= base[i]:
            tmp += 1
    R[i] = tmp


cnt = 0
for i in range(n):
    cnt += L[i] * R[i]
print(cnt)