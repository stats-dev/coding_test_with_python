n = int(input())

arr = [0] + list(map(int, input().split()))

def rec_max(n):
    if n == 0:
        return arr[0]

    test = rec_max(n-1)
    if arr[n] > test:
        return arr[n]
    else:
        return test
        
    
print(rec_max(n))