class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hi, I'm " + self.name)

class Police(Person):
    def arrest(self, to_arrest):
        print(to_arrest + ". You're under arrest.")

class Programmer(Person):
    def program(slef):
        print("I'm gonna code someting.")

tom = Person("Tom")
paul = Police("Paul")
jane = Programmer("Jane")

tom.introduce()
paul.introduce()
paul.arrest("Paul")
jane.introduce()
jane.program()
