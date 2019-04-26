#1. class

class Person:
    name = 'David'
    
    def say_hello(self):
        print(f"Hello, {self.name}")
        
dv = Person()
dv.say_hello()
print(dv.name)