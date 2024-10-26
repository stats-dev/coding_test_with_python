## 객체를 원소로

class Codename:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score


codenames = [Codename(*tuple(input().split())) for _ in range(5)]

min_cn = codenames[0]

for i in range(5):
    if int(codenames[i].score) < int(codenames[0].score):
        min_cn = codenames[i]

print(min_cn.codename, min_cn.score, end= " ")