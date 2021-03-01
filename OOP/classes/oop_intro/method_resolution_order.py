# Порядок разрешения методов

#   A
#  / \
#  B C
#  \ /
#   D

class A:
    def some_method(self):
        print("Method of class A")


class B(A):
    def some_method(self):
        print("Method of class B")


class C(A):
    def some_method(self):
        print("Method of class C")


class D(B, C):
    # Если мы не используем никакой атрибут объекта, можно сделать метод на уровне класса
    @classmethod
    def some_method(cls):
        print("Method of class D")


some_obj = D()
some_obj.some_method()

# Способы узнать какой метод будет вызван
# __mro__, mro(), help()

print(D.__mro__)
print(D.mro())
help(D)