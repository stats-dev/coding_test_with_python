n = int(input())

class Live:
    def __init__(self, name, num, region):
        self.name = name
        self.num = num
        self.region = region

lives = [
    Live(*input().split())
    for _ in range(n)
]

lives_last = max(lives, key = lambda x: x.name)


print(f"name {lives_last.name}\naddr {lives_last.num}\ncity {lives_last.region}")