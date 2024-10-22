Y, M, D = tuple(map(int, input().split()))

def is_yun(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def is_season(month):
    if month > 2:
        print("Spring")
    elif month > 5:
        print("Summer")
    elif month > 8:
        print("Fall")
    else:
        print("Winter")

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