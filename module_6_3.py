import random

# Класс Animal
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

# Класс Bird
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

# Класс AquaticAnimal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Берём модуль dz
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z

# Класс PoisonousAnimal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# Класс Duckbill
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

# Пример работы программы
db = Duckbill(10)

print(db.live)      # True
print(db.beak)      # True

db.speak()          # Click-click-click
db.attack()         # Be careful, i'm attacking you 0_0

db.move(1, 2, 3)
db.get_cords()      # X: 10 Y: 20 Z: 30

db.dive_in(6)
db.get_cords()      # X: 10 Y: 20 Z: 0

db.lay_eggs()       # Here are(is) <случайное число от 1 до 4> eggs for you
