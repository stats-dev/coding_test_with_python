n = int(input())

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


students = [
    list(tuple(input().split()))
    for _ in range(n)
]

arr = []

for student in students:
    arr.append(Student(*student))

arr.sort(key = lambda x : x.height)

for a in arr:
    print(a.name, a.height, a.weight)