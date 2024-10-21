def is_yunyear(n):
    ## 4로 나누어지면 윤년
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    elif n % 4 == 0:
        return "true"

    return "false"

y = int(input())

yun = is_yunyear(y)
print(yun)