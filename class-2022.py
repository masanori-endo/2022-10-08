class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_something(self):
        print(f'hello {self.name} age = {self.age}')

masa = Person('masa', 15)
masa.say_something()