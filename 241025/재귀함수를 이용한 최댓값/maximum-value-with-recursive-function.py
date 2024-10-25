n = int(input())

arr = [0] + list(map(int, input().split()))

def rec_max(n):
    if n == 0:
        return arr[0]

    
    if arr[n] > rec_max(n-1):
        return arr[n]
    else:
        return rec_max(n-1)
        
    
print(rec_max(n))