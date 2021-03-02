class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age, money=0, house=None):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    # Инфо о человеке
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.money}")
        print(f"House: {self.house}")

    # Стандарстные данные
    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    # Покупка дома
    def make_deal(self, money, house):
        self.money -= money
        self.house = house.name

    # Зарплата
    def earn_money(self, money):
        self.money += money
        print(f'Earned {money} money! Current value: {self.money}')

    # Хватит ли средств
    def buy_house(self, house, money):
        if (self.house != house and self.money > money):
            print(f"You have enough money to buy {house.name}")
            self.make_deal(money, house)
        else:
            print(f"You don't have enough money to buy {house.name}")


# Дома
class House:
    def __init__(self, area, price, name):
        self.area = area
        self.price = price
        self.name = name

    # Финальная цена
    def final_price(self, discount, money):
        buy_money = money - (int(money / 100 * discount))
        return buy_money


class SmallHouse(House):
    default_area = 40

    def __init__(self, price, name):
        House.__init__(self, SmallHouse.default_area, price, name)


if __name__ == "__main__":
    Human.default_info()

    counter = Human("Arkady", 25, 100000)
    counter.info()

    room = SmallHouse(100000, "Penthouse")

    counter.buy_house(room, room.price)

    counter.earn_money(2000000)
    counter.buy_house(room, room.price)

    counter.info()