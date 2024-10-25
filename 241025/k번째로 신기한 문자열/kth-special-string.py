n, k, T = input().split()
n, k = int(n), int(k)

lst = [input() for _ in range(n)]
words = []

for e in lst:
    if e.startswith(T):
        words.append(e)

words.sort()
print(words[k-1])