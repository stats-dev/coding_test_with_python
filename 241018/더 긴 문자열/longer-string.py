w1, w2 = input().split()

lw1 = len(w1)
lw2 = len(w2)

if lw1 == lw2:
    print("same")
else:
    if lw1 > lw2:
        print(w1, lw1)
    else:
        print(w2, lw2)