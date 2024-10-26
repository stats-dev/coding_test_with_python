class nextlevel:
    def __init__(self, user, lv):
        self.user = user
        self.lv = lv

user, lv = input().split()

nl = nextlevel(user='codetree', lv=10)

print("user", nl.user, "lv", nl.lv)

nl = nextlevel(user, lv)
print("user", nl.user, "lv", nl.lv)