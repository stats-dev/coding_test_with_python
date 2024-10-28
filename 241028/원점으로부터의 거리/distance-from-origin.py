n = int(input())

class Distance:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

dists = []

for i in range(1,n+1):
    x, y = tuple(map(int, input().split()))
    dists.append(Distance(int(x), int(y), i))

dists.sort(key = lambda x : (abs(x.x) + abs(x.y)))

for d in dists:
    print(d.num)