def palindrom(s):
    if (len(s) < 2):
        return True
    if (s[0] != s[-1]):
        return False
    return palindrom(s[1:-1])

a = str(input("Введите слово, чтобы проверить его на палиндром: "))
print(palindrom(a))