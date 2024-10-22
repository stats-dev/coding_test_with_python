m, d = map(int, input().split())

# def is_month(m, d):
#     throne = [1,3,5,7,8,10,12]
#     while m > 0 and m < 13:
#         if m == 2:
#             return d < 29
#         elif m in throne:
#             return d < 32
#         else:
#             return d < 31
#         return False

   
# if is_month(M, D):
#     print("Yes")
# else:
#     print("No")



def last_day_number(m):
    thr = [4,6,9,11]
    if m == 2:
        return 28
    elif m in thr:
        return 30
    return 31

def judge_day(m, d):
    if m <= 12 and d <= last_day_number(m):
        return True
    return False
 
 if judge_day(m, d):
    print("Yes")
else:
    print("No")