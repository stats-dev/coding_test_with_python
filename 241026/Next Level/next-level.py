# class nextlevel:
#     def __init__(self, user, lv):
#         self.user = user
#         self.lv = lv

# user, lv = input().split()

# nl = nextlevel(user='codetree', lv=10)

# print("user", nl.user, "lv", nl.lv)

# nl = nextlevel(user, lv)
# print("user", nl.user, "lv", nl.lv)


class User:
    def __init__(self, user_id="", level=0):
        self.user_id = user_id
        self.level = level


user1 = User()

user1.user_id = "codetree"
user1.level = 10


user2_id, level2 = tuple(input().split())

user2 = User()

user2.user_id = user2_id
user2.level = int(level2)


#출력을 한방에 : 리스트에 객체를 넣습니다. 이때는 객체 자체를 꺼내서 인스턴스를 출력시켜야 합니다.
for user in [user1, user2]:
    print(f"user {user.user_id} lv {user.level}")