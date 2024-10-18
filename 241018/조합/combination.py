n, m = map(int, input().split())

def facto(n):
    k = 1
    for i in range(1,n+1):
        k *= i
    return k


answer = 0

answer = int(facto(n) / (facto(m) * facto((n-m))))

print(answer)