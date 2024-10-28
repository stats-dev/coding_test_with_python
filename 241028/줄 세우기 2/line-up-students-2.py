n = int(input())

students = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

students.sort(key = lambda x: (x[0], -x[1]))

arr = [(s, idx) for s, idx in enumerate(students, start=1)]
# for student, idx in enumerate(students, start=1):
#     students.append(student)

for i in range(n):
    idx, (h, w) = arr[i]
    print(h, w, idx)