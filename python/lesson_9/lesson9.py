class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hey! My name is {self.name} and I am {self.age} years old.")

    def greet(self, name2):
        print(f"Hello {self.name}! I am {name2}")
    

a1= Animal('Akshita', 19)
a2= Animal('Prazzy', 19)
print(a1.name)
print(a1.age)
a1.intro()
a2.intro()

a1.greet('Prazzy')
a2.greet('Akshita')
      