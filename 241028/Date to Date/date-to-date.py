# month, day = 2, 5
# elapsed_days = 0

# #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# while True:
#     if month == 4 and day == 1:
#         break

#     elapsed_days += 1
#     day += 1

#     if day > num_of_days[month]:
#         month += 1
#         day = 1

# print(elapsed_days)

m1, d1, m2, d2 = map(int, input().split())
## 시작일
month, day = m1, d1

elapsed_days = 1 ##시작일 포함

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == m2 and day == d2:
        break
    
    elapsed_days += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_days)