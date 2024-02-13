#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

    def speak(self):
        return "Meow"

stella = Cat()
garfield = Cat()

stella.name = "Stella"
stella.age = 7

garfield.name = "Garfield"
garfield.age = 50

print(garfield.name, garfield.age, stella.name, stella.age)

stella.speak()
garfield.speak()