n = int(input())

class Student:
    def __init__(self, name, k, m):
        self.name, self.k, self.m = name, int(k), int(m)

students = []
    
for _ in range(n):
    name, k, m = tuple(input().split())
    students.append(Student(name, int(k), int(m)))

students.sort(key = lambda x: (x.k, -x.m))

for a in students:
    print(a.name, a.k, a.m)