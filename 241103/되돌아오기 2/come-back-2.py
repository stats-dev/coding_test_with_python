'''
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
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
 
    if x == 0 and y == 0:
        answer = time
        break

print(answer)
'''

dirs = input() ## 변수 선언 입력
x, y = 0, 0
currdir = 3 ## 3번이 왜 시작? 북쪽이라서?

## 동남서북 순 정의
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

# flag는 시작점으로 되돌아 왔는지 봅니다.
flag = False

leng = len(dirs)

## move
for i in range(leng):
    cdir = dirs[i]
    # re 90 rotate
    if cdir == 'L':
        currdir = (currdir - 1 + 4) % 4

    ## 90 +1 rotate
    elif cdir == 'R':
        currdir = (currdir + 1) % 4
    
    ## forward
    else:
        x, y = x + dxs[currdir], y + dys[currdir]
    
    # 00
    if x == 0 and y == 0:
        print(i + 1)
        flag = True
        break ## break 반드시 필요
    
## no return
if flag == False:
    print(-1)