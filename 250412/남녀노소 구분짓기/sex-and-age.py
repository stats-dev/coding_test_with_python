
agesex = [int(input()) for _ in range(2)]

if agesex[0] == 0:
    if agesex[1] >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if agesex[1] >= 19:
        print('WOMAN')
    else:
        print('GIRL')