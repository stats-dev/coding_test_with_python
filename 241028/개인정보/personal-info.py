students = [
    list(tuple(input().split()))
    for _ in range(5)
]

print("name")
students.sort(key = lambda x : x[0])
for s in students:
    print(s[0], s[1], s[2])
print()

print("height")
students.sort(key = lambda x : -int(x[1]))
for s in students:
    print(s[0], s[1], s[2])