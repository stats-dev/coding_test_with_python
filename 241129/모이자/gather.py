# n = 5
# arr = [1, 5, 2, 6, 8]

# max_sum = 0
# for i in range(n):
#     arr[i] *= 2

#     sum_diff = 0
#     for j in range(n - 1):
#         sum_diff += abs(arr[j + 1] - arr[j])

#     max_sum = max(max_sum, sum_diff)
#     arr[i] //= 2

# print(max_sum)
import sys

INT_MAX = sys.maxsize


n = int(input())

numbers = list(map(int, input().split()))

min_dist = INT_MAX

for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j - i) * numbers[j]

    ## 거리 합 최소
    min_dist = min(min_dist, sum_dist)

print(min_dist)
