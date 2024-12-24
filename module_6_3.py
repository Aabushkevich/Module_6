import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self,dx,dy,dz):
        new_dx = self._cords[0] + dx * self.speed
        new_dy = self._cords[1] + dy * self.speed
        new_dz = self._cords[2] + dz * self.speed
        if new_dz >= 0:
            self._cords = [new_dx,new_dy,new_dz]
        else:
            "It's too deep, i can't dive :("

    def get_cords(self):
        print(f'X:{self._cords[0]},Y:{self._cords[1]},Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacing you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'"Here are(is) {random.randint(1,4)} eggs for you"')

class AquaticAnimal(Animal):
    DEGREE_OF_DANGER = 3

    def dive_in(self,dz):
        dz = abs(dz)
        self._cords[2] -= int(dz / 2 * self.speed)
        if self._cords[2] < 0:
            self._cords[2] = 0

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    pass

class Duckbill(PoisonousAnimal,AquaticAnimal,Bird):
    sound = "Click-click-click"
    pass

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
