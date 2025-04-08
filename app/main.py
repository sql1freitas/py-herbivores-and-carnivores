class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)
        self._check_alive()

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def _check_alive(self):
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other.health = 0
        other._check_alive()