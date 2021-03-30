class AbstractCat:

    def __init__(self):
        self.weight = 0
        self.food_balance = 0

    def eat(self, food: int):
        food_with_balance = food + self.food_balance
        self.weight += food_with_balance // 10
        self.food_balance = food_with_balance % 10

    def __str__(self):
        return f'{self.__class__.__name__} ({self.weight})'


class Kitten(AbstractCat):

    def __init__(self, weight: int):
        super().__init__()
        self.weight = weight

    def meow(self):
        return "meow..."

    def sleep(self):
        return "Snore" * (self.weight // 5)


class Cat(Kitten):

    def __init__(self, weight: int, name: str):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return "MEOW..."

    def get_name(self):
        return self.name

    def catch_mice(self):
        return "Got it!"


if __name__ == '__main__':
    abscat = AbstractCat()
    abscat.eat(125)
    abscat.eat(17)
    print(abscat)
    kit = Kitten(21)
    print(kit.sleep())
    cat = Cat(83, 'Molly')
    print(cat.meow())
    print(cat.get_name())



