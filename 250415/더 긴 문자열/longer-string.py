sentences = list(input().split())

if len(sentences[0]) == len(sentences[1]):
    print('same')
elif len(sentences[0]) > len(sentences[1]):
    print('Coding ' + str(len(sentences[0])))
else:
    print('Coding ' + str(len(sentences[1])))