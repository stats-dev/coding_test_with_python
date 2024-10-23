instr = input()
obstr = input()

M = len(instr)
N = len(obstr)

def is_seq(s1, s2):
    for i in range(M - N + 1):
        if instr[i:i+N] == obstr:
            return i
    return -1

print(is_seq(instr, obstr))