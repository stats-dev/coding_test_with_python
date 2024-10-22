Y, M, D = tuple(map(int, input().split()))

def is_yun(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def is_season(month):
    if month in [3,4,5]:
        print("Spring")
    elif month in [6,7,8]:
        print("Summer")
    elif month in [9,10,11]:
        print("Fall")
    elif month in [12,1,2]:
        print("Winter")
    else:
        print(-1)

def is_last_day(year, month):
    if is_yun(year):
        if month == 2:
            return 29
    else:
        if month == 2:
            return 28
    
    if month in [4,6,9,11]:
        return 30
    else:
        return 31

if D <= is_last_day(Y, M):
    is_season(M)
else:
    print(-1)