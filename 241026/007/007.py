# kor1, eng1, math1 = 90, 80, 90

# ## class
# class Student:
#     def __init__(self, kor, end, math):
#         self.k = kor ## __init 생성자, self 항상 첫 인자. = 멤버변수
#         self.e = eng
#         self.m = math

# ## instance 객체
# student1 = Student(90, 80, 90)
# print(student1.k)
# print(student1.e)
# print(student1.m) ## self 뒤의 값으로 호출해요.


class codetree:
    def __init__(self, code, place, time):
        self.c = code
        self.p = place
        self.t = time

c, p, t = input().split()
secret = codetree(c, p, t)
print("secret code :", secret.c)
print("meeting point :", secret.p)
print("time :", secret.t)