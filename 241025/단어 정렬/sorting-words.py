# n = int(input())

# strs = [input() for _ in range(n)]


# strs.sort()

# for e in strs:
#     print(e)

import sys

n = int(input())
strs = sys.stdin.readlines()
# strs = [str.strip() for str in strs]
strs = [s.strip() for s in strs]
strs.sort()

for e in strs: print(e)