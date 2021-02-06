class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayhello(self, to_name):
        print("Hi, " + to_name + ". My name is " + self.name)
    def introduce(self):
        print("I'm " + str(self.age) + " old.")

yally = Person("Yally", 20)
yally.sayhello("Kristal")
yally.introduce()
