# num = 2
# x, y = 1, 5
# dx, dy = [1,0,-1,0], [0,-1,0,1]

# nx, ny = x + dx[num], y + dy[num]

n = int(input())


x, y = 0, 0

dx, dy = [1,0,-1,0], [0,-1,0,1]

E, S, W, N = 0, 1, 2, 3


for _ in range(n):
    arr = input().split()
    dr, dt = arr[0], int(arr[1])

    if dr=='N':
        d_num=3

    elif dr=='E':
        d_num=0

    elif dr=='S':
        d_num=1

    else:
        d_num=2

    
    x,y=x+dt*dx[d_num],y+dt*dy[d_num]

print(x, y)