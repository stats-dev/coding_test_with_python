a, b, c, d = map(int, input().split())


hour = c - a
mins = d - b

total = hour * 60 + mins
print(total)