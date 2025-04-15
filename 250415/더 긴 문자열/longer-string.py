sentences = list(input().split())

if len(sentences[0]) == len(sentences[1]):
    print('same')
elif len(sentences[0]) > len(sentences[1]):
    print(sentences[0] + ' ' + str(len(sentences[0])))
else:
    print(sentences[1] + ' ' + str(len(sentences[1])))