n = int(input())


def test_rec(n):

    if n == 1:
        return 0
    
    if n % 2 == 0:
        return test_rec(n // 2) + 1
    else:
        return test_rec(n * 3 + 1) + 1

print(test_rec(n))