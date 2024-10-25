n = int(input())

nlst = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b) ## 최소공배수는 두 수의 곱을 최대공약수로 나눔

def lcm_rec(lst):
    ## 재귀적으로 최소 공배수 구하기
    ## 종료 조건
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lcm(lst[0], lst[1])

    if len(lst) > 2:
        return lcm(lst[0], lcm_rec(lst[1:]))
    
result = lcm_rec(nlst)
print(result)