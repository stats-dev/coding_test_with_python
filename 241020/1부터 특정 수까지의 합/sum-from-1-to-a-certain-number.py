N = int(input())

def add_N(N):
    num = 0
    for i in range(1, N+1):
        num += i
    return num

result = add_N(N) // 10
print(result)