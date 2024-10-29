a,b,c = map(int, input().split())


day, hour, mins = 11, 11, 11
elapsed_days = 0

if a < day:
    print(-1)
elif a == day and b < hour:
    print(-1)
elif a == day and b == hour and c < mins:
    print(-1)
else:
    print((a - day) * 24 * 60 + (b - hour) * 60 + (c - mins))


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