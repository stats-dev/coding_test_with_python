n = int(input())

class Student:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, int(kor), int(eng), int(math)


students = [

    list(tuple(input().split()))
    for _ in range(n)
]


arr = []

for s in students:
    arr.append(Student(*s))

arr.sort(key = lambda x : (-x.kor, -x.eng, -x.math))

for student in arr:
    print(student.name, student.kor, student.eng, student.math)