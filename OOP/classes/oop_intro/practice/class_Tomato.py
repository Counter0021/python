class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index, state=0):
        self.index = index
        self.state = state

    # Вывод стадии на экран
    def print_state(self):
        print(f'Tomato {self.index} is {Tomato.states[self.state]}')

    # Следующая стадия
    def change_state(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    # Перевод на следующую стадию созревания
    def grow(self):
        self.change_state()

    # Достиг ли созревания
    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(0, count - 1)]

    # Перевод на следующую стадию
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    # Все созрели?
    def is_ripe_all(self):
        count = 0
        for i in self.tomatoes:
            if i.is_ripe():
                count += 1
        if count == len(self.tomatoes):
            print("All tomatoes are ripe")
            self.give_away_all()
            return True
        return False

    # Очистка после созревания
    def give_away_all(self):
        print("Harvesting is over")
        self.tomatoes.clear()


class Gardner:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    # Работать. Растение растёт быстрее
    def work(self):
        print("The gardener works")
        self.plant.grow_all()
        print("Plants have matured")

    # Всё ли созрело?
    def harvest(self):
        print('Gardener is harvesting...')
        if self.plant.is_ripe_all():
            self.plant.give_away_all()
            print("Harvesting is finished")
        else:
            print("Too early! Your plant is green and not ripe")

    # Садовник
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur when the fruit is a mature green and \
then allowed to ripen off the vine. 
This prevents splitting or bruising \
and allows for a measure of control over the ripening process.''')
        print()


if __name__ == "__main__":
    Gardner.knowledge_base()
    tomato = TomatoBush(5)
    gard = Gardner("Counter", tomato)
    gard.work()
    gard.harvest()
    tomato.grow_all()
    tomato.grow_all()
    gard.harvest()