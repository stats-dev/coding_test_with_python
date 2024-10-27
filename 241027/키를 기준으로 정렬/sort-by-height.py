class Body:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

n = int(input())

infos = [
    Body(*input().split())
    for _ in range(n)
]

infos.sort(key=lambda x : x.tall)

for e in infos:
    print(e.name, e.tall, e.weight)