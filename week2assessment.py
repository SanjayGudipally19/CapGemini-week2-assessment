# #1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
class Employee:
    def __init__(self,name,empid,department):
        self.name=name
        self.empid=empid
        self.department=department
    def display(self):
        print(f"details: your name is {self.name} and your emp id is {self.empid} and you belong to {self.department} department")
name=input("enter name: ")
empid=input("enter your id: ")
department=input("enter your department: ")
emp=Employee(name,empid,department)
emp.display()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
        print(f"your current balance is {self.balance}")
    def deposit(self,money):
        self.balance+=money
        print(f"money added successfully and your current balance is {self.balance}")
    def withdraw(self,money):
        if money>self.balance:
            print("insufficient balance")
        else:
            self.balance-=money
            print(f"money withdrawn successfully and your current balance is {self.balance}")
acc=Bankaccount(5000)
acc.deposit(2000)
acc.withdraw(6000)
acc.withdraw(4000)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"Book details are:\ntitle:{self.title}\nauthor:{self.author}\nisbn:{self.isbn}")
book=Book("mybook","sanjay",1256)
book.display()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        return (f"student name is : {self.name}\nroll number is :{self.roll}")
student1=Student("sanjay","5g0")
result=student1.display()
print(result)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if (quantity > self.stock):
            return ("requested quantity is not available")
        else:
            return ("requested quantity is available")
p1=Product("bat",5000,100)
result=p1.check_availability(50)
print(result)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self):
        pass
    def startEngine(self):
        print("The vehicle is started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def openBoot(self):
        print("The car boot is opened")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
    def openTank(self):
        print("The bike's petrol tank is opened")
class ElectricCar(Car):
    def __init__(self,battery_capacity):
        super().__init__()
        self.battery_capacity = battery_capacity
    def displayElectricCarInfo(self):
        print(f'battery capacity is {self.battery_capacity}Kw')
ec = ElectricCar(100)
ec.displayElectricCarInfo()
ec.openBoot()
b1 = Bike()
b1.openTank()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name is {self.name}")
class Employee(Person):
    def __init__(self, name,empid):
        super().__init__(name)
        self.empid=empid
    def display(self):
        print(f"name is {self.name} and emp id is {self.empid}")
class Manager(Employee):
    def __init__(self, name, empid):
        super().__init__(name, empid)
    def approve_leave(self):
        print(f"leave granted for {self.name} whose empid is {self.empid}")
p1=Manager("sanjay","5g0")
p1.approve_leave()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal:
    def speak(self):
        print("animal shouted")
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("dog barked")
class Cat(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("cat said meow")
a=Animal()
a.speak()
b=Dog()
b.speak()
c=Cat()
c.speak()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        print("car is moving")
        super().move()
class Airplane:
    def move(self):
        print("airplane is moving")
class FlyingCar(Car, Airplane):
    def move(self):
        super().move()
        print("flying car is moving")
a = FlyingCar()
a.move()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"brand is {self.brand} and model is {self.model}")
class MobileDevice(Electronics):
    def __init__(self,brand,model,price):
        super().__init__(brand,model)
        self.price=price
    def display(self):
        print(f"brand is {self.brand} and model is {self.model} and price is {self.price}")
class SmartPhone(MobileDevice): 
    def __init__(self,brand,model,price,size):
        super().__init__(brand,model,price)
        self.size=size
    def display(self):
        print(f"brand is {self.brand} and model is {self.model} and price is {self.price} and size is {self.size}")
s=SmartPhone("poco","x3",20000,"6inch")
s.display()
m=MobileDevice("samsung","galaxy",50000)
m.display()
e=Electronics("samsung","galaxy")
e.display()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self, message, type="info"):
        print(f"{type}: {message}")
l = Logger()
l.log("this is error", "error")
l.log("this is warning", "warning")  
l.log("this is info")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def process_payment(self):
        print("payment processed")
class CreditCardPayment(Payment):
    def process_payment(self):
        print("credit card payment processed")
class PayPalPayment(Payment):
    def process_payment(self):
        print("paypal payment processed")
class BitcoinPayment(Payment):
    def process_payment(self):
        print("bitcoin payment processed")
p=Payment()
p.process_payment()
c=CreditCardPayment()
c.process_payment()
p=PayPalPayment()
p.process_payment()
b=BitcoinPayment()
b.process_payment()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        print("area of shape")
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(self.side*self.side)
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print(0.5*self.base*self.height)
a=Shape()
a.area()
s=Square(10)
s.area()
t=Triangle(515,10)
t.area()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        print("notification sent")
class Emailnotification(Notification):
    def send(self):
        print("email sent")
class Smsnotification(Notification):
    def send(self):
        print("sms sent")
n=Notification()
n.send()
e=Emailnotification()
e.send()
s=Smsnotification()
s.send()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC, abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calculate_area(self):
        print(self.l*self.b)
class Circle(IShape):
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        print(3.14*self.r*self.r)
r=Rectangle(10,20)
r.calculate_area()
c=Circle(5)
c.calculate_area()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    def display(self):
        print("iam abstract class")
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("inserted in SQL")
    def update(self):
        print("updated in SQL")
    def delete(self):
        print("deleted in SQL")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("inserted in NoSQL")
    def update(self):
        print("updated in NoSQL")
    def delete(self):
        print("deleted in NoSQL")
s=SQLDatabase()
s.insert()
s.update()
s.delete()
n=NoSQLDatabase()
n.insert()
n.update()
n.delete()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
from abc import ABC, abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
    def display(self):
        print("iam abstract class")
class BasicCalculator(ICalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def subtract(self):
        print(self.a-self.b)
    def multiply(self):
        print(self.a*self.b)
    def divide(self):
        print(self.a/self.b)
b=BasicCalculator(10,5)
b.add()
b.subtract()
b.multiply()
b.divide()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC, abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("bike engine started")
    def stop_engine(self):
        print("bike engine stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("truck engine started")
    def stop_engine(self):
        print("truck engine stopped")
c=Car()
c.start_engine()
c.stop_engine()
b=Bike()
b.start_engine()
b.stop_engine()
t=Truck()
t.start_engine()
t.stop_engine()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("google login")
    def logout(self):
        print("google logout")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("facebook login")
    def logout(self):
        print("facebook logout")
g=GoogleAuth()
g.login()
g.logout()
f=FacebookAuth()
f.login()
f.logout()
