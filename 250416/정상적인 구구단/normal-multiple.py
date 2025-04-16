n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j % 3 == 0:
            print(f"{i} * {j} = {i*j}", end=" ")
        else:
            print(f"{i} * {j} = {i*j},", end=" ")
    print()