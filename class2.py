class Person:
    def __init__(self, name):
        self.name = name
    def sayhello(self):
        print("Hi, My name is " + self.name)

yally = Person("Yally")
jane = Person("Jane")
kristal = Person("Kristal")

yally.sayhello()
jane.sayhello()
kristal.sayhello()
