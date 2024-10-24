n = int(input())

def fn_rec(n):
    if n == 0:
        return
    print(n, end= " ")
    fn_rec(n-1)
    print(n, end=" ")

fn_rec(n)