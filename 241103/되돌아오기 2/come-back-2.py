## 시작
x, y = 0, 0

## 좌표에 딱히 제한이 없음.

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 3 ## 0, 1, 2, 3 오, 아, 왼, 위 왼부터 시작?


time = 0
answer = -1 ## flag
## 회전하는 것에 유의한다.

direcs = input()

for d in direcs:
    time += 1
    if d == 'F': ## 이건 이동해야함.
        x += dxs[dir_num]
        y += dys[dir_num]
    elif d == 'L':
        dir_num = (dir_num - 1) % 4
    else:
        dir_num = (dir_num + 1) % 4
 
    if x == 0 and y == 0:
        answer = time

print(answer)