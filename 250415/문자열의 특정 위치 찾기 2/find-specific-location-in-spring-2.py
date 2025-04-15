arr = ["apple","banana","grape","blueberry","orange"]

string = input()
cnt = 0
for word in arr:
    if word[3-1] == string or word[4-1] == string:
        cnt += 1
        print(word)
print(cnt)
        