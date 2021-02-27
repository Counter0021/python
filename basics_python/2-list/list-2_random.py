from random import randint

N = 3
M = 4

a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(1, 99))
    a.append(b)
print(a, end="\n\n")
for i in range(N):
    for j in range(M):
        print("%3d" % a[i][j], end="")
    print()