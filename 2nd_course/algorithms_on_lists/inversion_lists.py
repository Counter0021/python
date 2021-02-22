a = [5, 3, 1, 9, 4, 3, 2]

print(f"До инверсии: {a}")

for i in range(len(a) // 2):
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

print(f"После инверсии: {a}")