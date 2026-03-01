class Animal:
    def __init__(self,sound):
        self.sound=sound
    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self,sound):
        super().__init__(sound)

d1=Dog("Bark")
d1.make_sound()