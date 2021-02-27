# Список от 1 до 10
a = [i+1 for i in range(10)]
print(a)
b = {str(i + 1): i + 1 for i in range(10)}
print(b)
c = [(i+1, (i+1) / 2) for i in range(4)]
print(c)
d = [i+j for i, j in c]
print(d)

# Двойной for
s1 = "abcd"
s2 = "01"
s = [i+j for i in s1 for j in s2]
print(s)
# Аналог
k = []
for i in s1:
    for j in s2:
        k.append(i + j)
print(k)

# С if
e = [i for i in a if (i % 2 == 0)]
print(e)
# Аналог
l = []
for i in a:
    if (i % 2 == 0):
        l.append(i)
print(l)

# Двойно for и if
f = [1, 2, 3]
g = [4, 5, 6]
h = [(i, j) for i in f for j in g if (i * j <= 10)]
print(h)

# Аналог
m = []
for i in f:
    for j in g:
        if (i * j <= 10):
            m.append((i, j))
print(m)