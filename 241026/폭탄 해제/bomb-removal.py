class Bomb: ##upper
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec


cd, cl, s = tuple(input().split())

bomb = Bomb(cd, cl, s)
print(f"code : {bomb.code}\ncolor : {bomb.color}\nsecond : {bomb.sec}")