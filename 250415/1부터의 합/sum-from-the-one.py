n = int(input())

sum1 = 0
for i in range(1,100+1):
    sum1 += i
    if sum1 >= n:
        print(i)
        break
    