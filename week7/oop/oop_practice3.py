#1
class Animal:

    def speak():
        return "..."
    

class Dog(Animal):

    def speak():
        return "woof!"
    

#2
class Train:
    def __init__(self, len, speed=60):
        self.__len = len
        self.speed = speed
#        self.stop()

    def go(self):
        return f"train is going at {self.speed}"
    
    @property
    def length(self):
        return self.__len
    
    @length.setter
    def length(self, new_len):
        if new_len > 0:
            self.__len = new_len
        return True
    
    def stop(self):
        self.speed = 0

    @classmethod
    def create_train(cls, tpl):
        return cls(tpl[0], tpl(1))


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    @property
    def price(self):
        return self.price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self._pric = value

a=Product('kobi',100)
print(a.price)
# a.price=200
# print(a._pric)
# print(a.price)

