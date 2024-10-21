def min_args(*args):
    #print(f"args: {args}")
    return min(args)

a,b,c = map(int, input().split())

result = min_args(a,b,c)

print(result)