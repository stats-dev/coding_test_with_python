string = [input() for _ in range(2)]


len_str = 0
for str in string:
    len_str += len(str)

print(len_str)