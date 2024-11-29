blank = list(input()) ## 빈칸 필요한데,

answer = 0

for i in range(len(blank)):
    for j in blank[i:]:
        if blank[i]+j=='()':
            answer += 1

print(answer)

