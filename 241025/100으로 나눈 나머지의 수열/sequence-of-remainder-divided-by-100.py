N = int(input())

def rem_seq(n):
    if n == 1:
        return 2
    
    if n == 2:
        return 4
    
    if n > 2:
        return rem_seq(n-1) * rem_seq(n-2) % 100

print(rem_seq(N))