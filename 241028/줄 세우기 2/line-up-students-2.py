n = int(input())

students = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr = [(s, idx) for s, idx in enumerate(students, start=1)]


arr.sort(key = lambda x: (x[1][0], -x[1][1]))

for i in range(n):
    idx, (h, w) = arr[i]
    print(h, w, idx)

# for student, idx in enumerate(students, start=1):
#     students.append(student)

# for i in range(n):
#     idx, (h, w) = arr[i]
#     print(h, w, idx)