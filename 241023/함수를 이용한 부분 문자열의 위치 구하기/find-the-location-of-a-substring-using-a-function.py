s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

def is_part(s1, s2):
    for i in range(n1 - n2 + 1):
        if s1[i:i + n2] == s2:
            return i
    return -1

print(is_part(s1, s2))