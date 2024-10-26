## 객체를 원소로

class Codename:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score


codenames = [Codename(*tuple(input().split())) for _ in range(5)]

# min_cn = Codename()

# if codenames:
#     min_cn = codenames[0]
#     for code in codenames:
#         if int(code.score) < int(min_cn.score):
#             min_cn = code

##혹은 lambda x : min(int(x.score)) 를 활용할 수 있음.

min_cn = min(codenames, key = lambda x : int(x.score))


print(min_cn.codename, min_cn.score, end= " ")