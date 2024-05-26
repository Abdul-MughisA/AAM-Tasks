class Animal:

    # private age
    # private vertebrae

    # public procedure sound

    def __init__(self, vertebrae):
        self.age = 0                # private
        self.vertebrae = vertebrae  # private
    #end def: constructor

    def sound(self):
        pass
    #end def: procedure
#end class

class Mammal(Animal):
    def __init__(self, legs):
        self.legs = legs
        super().__init__(True)
    #end def: constructor
#end class

class Dog(Mammal):
    def sound(self):
        print("Woof!")
#end class

class Cat(Mammal):
    def sound(self):
        print("Meow!")
#end class

Dog1 = Dog(4)
Cat1 = Cat(4)

Dog1.sound()
Cat1.sound()
