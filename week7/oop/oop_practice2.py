# 1
class Student:
    def __init__(self, name):
        self.name = name

    @property
    def name_get(self):
        return self.name


# 2
class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    @property
    def area(self):
        return self.width * self.hight


a = Rectangle(3, 4)


# 4
class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if self.balance <= 0:
            print("not enough money")
            return
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount


a = BankAccount()


# 5
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


# 6
class Temperature:
    def __init__(self):
        self._temperature = 0

    @property
    def fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def fahrenheit(self, temp):
        self._temperature = (temp - 32) / 1.8


a = Temperature()
a.fahrenheit = 104


# 7
class Calculator:

    @staticmethod
    def is_even(n):
        return n % 2 == 0


a = Calculator()


# 8
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])


# 9
class User:
    uses = 0

    def __init__(self):
        User.uses += 1

    @classmethod
    def how_many(cls):
        return cls.uses


a = User()
b = User()


# 10
class Product:
    def __init__(self):
        self._name = ""
        self.__price = 0

    @property
    def name(self):
        return self._name

    def name(self, new):
        self._name = new

    @property
    def price(self):
        return self.__price

    def price(self, new):
        if new < 0:
            print("can't set the price to negative")
            return
        self.__price = new

a = Product()