arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    print(sum(arr_2d[i]) / 4, end = ' ')
print()

sum1 = 0
sum2 = 0
for i in range(4):
    sum1 = 0
    sum1 = arr_2d[0][i] + arr_2d[1][i]
    sum2 += sum1
    print(sum1 / 2, end = ' ')
print()
print(sum2 / 8)