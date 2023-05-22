class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet 

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self



class Pets(Ninja):
    def __init__(self, pet_name, pet_type, tricks, hubbub):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.tricks = tricks
        self.hubbub = hubbub
        self.health = 1000
        self.energy = 1000

        
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        print(f'Drogon flames the defiant - he eats well today!')
        return self

    def play(self):
        self.health += 5
        self.energy += 15
        print(f'Drogon is obstinate and prefers to fly - you are left behind choking on dust')
        return self

    def noise(self):
        print(f'Drogon Shivers, shakes off water & roars: How can you just leave me standing alone in a world so cold? (World so cold)')
        return self

dragon_Treats = ('an occasiona lamb','an errant waif', "armored soldery", "pesky scorpions")
dragon_Chow = ('the peasantry', 'surly royals', 'defiant nobelmen')

Drogon = Pets("Drogon", "Crotchety Old Dragon", "not burning the living", "ROAR")
SubZero = Ninja("Kuai","Liang", dragon_Treats, dragon_Chow, Drogon)

SubZero.walk()
SubZero.feed()
SubZero.bathe()