N = int(input())

cnt = 0
def forone(N):
    global cnt
    if N == 1:
        return cnt
    
    if N % 2 == 0:
        forone(N // 2)
        cnt += 1
        return cnt
    else:
        forone(N // 3)
        cnt += 1
        return cnt
    

print(forone(N))