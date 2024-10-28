n = int(input())

seq = list(tuple(map(int, input().split())))

seq_idx_org = [(idx, s) for idx, s in enumerate(seq, start=1)]

seq_idx_org.sort(key = lambda x : x[1])

seq_idx_org2 = [(idx, s) for idx, s in enumerate(seq_idx_org, start = 1)]
# seq_idx = [(idx, s, y) for idx, s, y in enumerate(seq, start=1)]

seq_idx_org2.sort(key = lambda x: x[1][0])

for s in seq_idx_org2:
    print(s[0], end= " ")