ab=input()
arr = ab.split()
intarr = [int(a) for a in arr]
print(arr[0], arr[1], sum(intarr))