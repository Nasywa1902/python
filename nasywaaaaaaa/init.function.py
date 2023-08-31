class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is ", self.name)

person1 = Person("nasywa")
person1.say_hi()