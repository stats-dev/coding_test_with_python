n, m = map(int, input().split())

A = [0] + list(map(int, input().split()))
test = []

for _ in range(m):
    a1, a2 = tuple(map(int, input().split()))
    test.append((a1, a2))

def sum_per():
    global A
    sum_val = 0
    for i,j in test:
        sum_val = sum(A[i:j+1])
        print(sum_val)

sum_per()