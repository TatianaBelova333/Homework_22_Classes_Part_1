class Warrior:
    def attack(self):
        pass

    def defend(self):
        pass

    def move(self):
        pass

class Healer:
    def defend(self):
        pass

    def move(self):
        pass

    def heal(self):
        pass


class Tree:
    def defend(self):
        pass

    def burn(self):
        pass


class Trap:
    def attack(self):
        pass

if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()