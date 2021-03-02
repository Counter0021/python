# Алфавит
class Alphabet:

    def __init__(self, lang="eng", letters=str):
        self.lang = lang.upper()
        self.letters = letters.split(' ')

    # Делаем вывод при помощи print()
    def __str__(self):
        return f"Letters in {self.lang} alphabet {self.letters}"

    # Сколько букв в алфавите
    def letters_num(self):
        return f"There are {len(self.letters)} letters in the {self.lang} alphabet"


# Алфавит Eng
class EngAlphabet(Alphabet):
    # Количество букв
    __letters_num = 26

    def __init__(self, lang, letters):
        Alphabet.__init__(self, lang, letters)

    # Есть ли буква в Eng языке
    def is_en_letter(self, letter):
        if (letter.lower() in self.letters):
            return f"The letter '{letter}' is in the {self.lang} alphabet "
        else:
            return False

    # Сколько букв в Eng языке
    def letters_num(self):
        return f"There are {EngAlphabet.__letters_num} letters in the {self.lang} alphabet"

    # Статический метод для вывода текста на англ. языке
    @staticmethod
    def example():
        print("Helloy! Today is a wonderful day!")


if __name__ == "__main__":
    # Строки букв
    str_rus_letters = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
    str_eng_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    rus = Alphabet("rus", str_rus_letters)
    print(rus)
    print(rus.letters_num())

    eng = EngAlphabet("eng", str_eng_letters)
    print(eng)
    print(eng.letters_num())
    eng.example()
    print(eng.is_en_letter("q"))
