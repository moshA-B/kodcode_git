#1
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says 'woof'"
    
Dog("rex").bark()

#2
class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def area(self):
        return self.width * self.hight
    
#3
class Counter:
    n = 7
    def  __init__(self, start=0):
        self.start = start

    def increment(self):
        self.start += 1
    
    def value(self):
        return self.start

c = Counter()  
#4
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"hello"

p = Point(1,2)
print(p)

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def withdraw(self, amount):
        if self.balance <= 0:
            print("not enough money")
            return
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

   
          
bank = BankAccount()
bank.withdraw(500)
print(bank.balance)

#6
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * (9/5)) + 32
    

#7
class Student:
    school = "kodcode"
    def __init__(self, name):
        self.name = name


#8
class Player:
    Counter = 0
    def __init__(self):
        Player.Counter += 1


#9
class Money:
    def __init__(self, amount):
        self.amount = amount

    def is_more_then(self, other):
        return self.amount > other.amount
    

a = Money(100)
b = Money(200)
b.is_more_then(a)


#10
class Playlist:
    def __init__(self):
        self.songs = [1,2,3,4]

    def add(self, title):
        self.songs.append(title)

    def remove(self, title):
        self.songs.remove(title)

    def count(self):
        return len(self.songs)
    
    def __str__(self):
        return f"{self.songs}"
a = Playlist()
a.add(5)
print(a)
