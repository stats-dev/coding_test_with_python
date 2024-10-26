## 객체를 원소로

class Codename:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score


codenames = [Codename(*tuple(input().split())) for _ in range(5)]

min_cn = Codename()

if codenames:
    min_cn = codenames[0]
    for code in codenames:
        if int(code.score) < int(min_cn.score):
            min_cn = code

print(min_cn.codename, min_cn.score, end= " ")