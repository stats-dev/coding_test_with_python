## 시작
x, y = 0, 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

dir_num = 0

time = 0
answer = -1 


dlists = input()

for d in dlists:
    time += 1

    if d == 'F':
        x += dxs[dir_num]
        y += dys[dir_num]
    elif d == 'L':
        dir_num = (dir_num - 1) % 4
    else:
        dir_num = (dir_num + 1) % 4
    
    if x, y == 0, 0:
        answer = time

print(answer)