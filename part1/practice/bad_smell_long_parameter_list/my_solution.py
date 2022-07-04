class Unit:

    def __init__(self, field, x_coord, y_coord, state, speed=1):
        self.field = field
        self.state = state
        self.speed = speed
        self.x = x_coord
        self.y = y_coord

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Так невозможно передвигаться')


if __name__ == '__main__':
    hero = Unit('f', 1, 2, 'fly')
    print(hero.move('UP'))
    print(hero.x)