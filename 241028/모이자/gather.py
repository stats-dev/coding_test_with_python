# n = 5
# arr = [1, 5, 2, 6, 8]



# max_sum = 0
# for i in range(n):
#     arr[i] *= 2

#     sum_diff = 0
#     for j in range(n - 1):
#         sum_diff += abs(arr[j + 1] - arr[j]) ##절대값의 차이

    
#     max_sum = max(max_sum, sum_diff)
#     arr[i] //= 2

# print(max_sum)

n = int(input())

dists = list(map(int, input().split()))

import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

min_val = INT_MAX

for i in range(n):
    sum_dists = 0
    for j in range(n):
        sum_dists += dists[j] * abs(i - j) ## i번째의 집이라고 하면, i * 0이고 나머지는, i-j의 거리
    if min_val > sum_dists:
        min_val = sum_dists

print(min_val)