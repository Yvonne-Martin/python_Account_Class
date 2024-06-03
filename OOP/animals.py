class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def skin(self):
        pass
class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("The bird is flying")
    def skin(self):
        print(":I have feathers")
class Fish(Animal):
    def make_sound(self):
        print("click")
    def move(self):
        print("I love Swimming")
    def skin(self):
        print("I have scales")
class Dog(Animal):
    def make_sound(self):
        print("bark")
    def move(self):
        print("walk")
    def skin(self):
        print("I have Fur")
class Human_being(Animal):
    def make_sound(self):
        print("Talk")
    def move(self):
        print("I walk")
    def skin(self):
        print("I have epidermis")