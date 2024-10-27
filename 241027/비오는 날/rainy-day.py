class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

weathers = [Weather(*input().split()) for _ in range(n)]
rains = [w for w in weathers if w.weather == 'Rain']

if rains:
    closed_rains = min(rains, key = lambda x : x.date)

print(f"{closed_rains.date} {closed_rains.day} {closed_rains.weather}")