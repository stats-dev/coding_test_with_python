## class

class Student:
    def __init__(self, height, weight, rank):
        self.height = height
        self.weight = weight
        self.rank = None

# for rank, num in enumerate(numx, start=1):
#     num_to_rank[num] = rank

## 키 내림차순, 몸무게, 번호 내림차순
# 번호를 먼저 지정함. rank, enumerate 활용
n = int(input())

students = [
    list(tuple(map(int, input().split())))
    for _ in range(n)
]


arr = []

for student in students:
    height, weight = student
    arr.append(Student(height, weight, 0))


for idx, s in enumerate(arr, start=1):
    s.rank = idx

arr.sort(key = lambda x : (-x.height, -x.weight, x.rank))

for s in arr:
    print(s.height, s.weight, s.rank)