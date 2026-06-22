class Animal:
    def speak(self):
        print("Animal sound is louder")
class Cat(Animal):
    def speak(self):
        print("meaow")
class Dog(Animal):
    def speak(self):
        print("Dogs")
C=Cat()
D=Dog()
C.speak()
D.speak()

#constructor
# class Car:
#     def __init__(self,brand,name):
#         self.brand=brand
#         self.name=name
#         print("Brand",brand,"Name",name)
#     def display(self):
#         print(f"Brand:{self.brand},Name:{self.name}")

# c=Car("BMW","5 series")
# c1=Car("Benz","BENZ3200d")
# c.display()
# c1.display()

#ACCOUNT
class Account:
    #constrcutor

    def __init__(self,name="",num=0,bal=0.0):
        print("Constructor called")
        self.__holder=name
        self.__accNum=num
        self.__accBal=bal
    
    def __add__(self, other):
        self.__accBal+=other
        print(other,"credited",self.__accNum)
    def __sub__(self, other):
        if self.__accBal>=other:
            self.__accBal-=other
            print(other,"debited",self.__accNum)

        else:
            print(self.__accNum,"Insufficeint_balance")

    def __str__(self):
        return self.__holder+"\n"+str(self.__accNum)+"\n"+str(self.__accBal)+"\n"

    def setHolder(self, name=""):
        self.__holder = name 
    def getHolder(self):
        return self.__holder
    def setAccNum(self,num=0):
        self.__accNum=num
    def getAccNum(self):
        return self.__accNum
    def setAccBal(self,bal=0.0):
        self.__accBal=bal
    def getAccBal(self):
        return self.__accBal

acc1=Account()
acc1.setAccNum(124523) 
acc1.setAccBal(1500.0)
acc1.setHolder("Gowthami") 
print(acc1)
acc1+5000
print(acc1)
         
#Single Inheritance
class Car:
    def steering(self):
        print("Comfortable to ride")
class Bike(Car):
    def Gear(self):
        print("^ six Speed Gear Box")
c=Bike()
c.steering() 
c.Gear()               

#Single Inheritance
class Car:
    def steering(self):
        print("Comfortable to ride")
class Bike(Car):
    def Gear(self):
        print("^ six Speed Gear Box")
c=Bike()
c.steering() 
c.Gear()         

class Car:
    def Wheel(self):
        print("ALLOY WHEEELS")
class Benz(Car):
    def Luxury(self):
        print("Its a Costlier car ")
class BYD(Benz):
    def Comfort(self):
        print("BYD Compare to Benz")
b=BYD()
b.Wheel()
b.Comfort()
b.Luxury()

class Travels:
    def busname(self):
        print("Swamy Ayyappa")
class Travels1:
    def bustype(self):
        print("VOlvo 9600 SLX")

class main_class(Travels,Travels1):
    def Price(self):
        print("3500RS")
M=main_class()
M.busname()
M.bustype()
M.Price()

class sam:
    def Add(self,a):
        print(a)
    def Add(self,a,b):
        print(a+b)
    def Add(self,a,b,c):
        print(a+b+c)
s=sam()
# s.Add(10)
# s.Add(10,20)
s.Add(10,20,30)

class Load:
    def loading(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
l=Load()
print("Add",l.loading(125))
print("Add",l.loading(125,125))
print("Add",l.loading(125,125,125))

class Payment:
    def pay(self,amount):
        print(f"Paying,{amount}")
class creditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} credit card") 
class Upi(Payment):
    def pay(self,amount):
        print(f"Paid {amount} UPI MODE")
Payment=[creditCard(),Upi()]

for a in Payment:
    a.pay(5000)
             
class Dhanya:
    def name(self):
        print("Dhanya cluny")
class Asmitha(Dhanya):
    def name(self):
        super().name()
        print("Asmitha cluny")    
class Aswathi(Asmitha):
    def name(self):
        super().name()
        print("Aswathi cluny")
class Aishwarya(Aswathi):
    def name(self):
        super().name()
        print("Aishwarya cluny")        
A=Aishwarya()
dA.name()  
#A.name()      

from abc import ABC
class bus(ABC):
    def volvo(self):
        print("Luxury Bus")
class Lorry(bus):
    def volvo(self):
        print("Happy")
class Car(bus):
    def volvo(self):
        print("COstlier car")
A=bus()
A.volvo()                
l=Lorry()
l.volvo()
c=Car()
c.volvo()

class Mobile:
    __model=""   #private
    __price=0.0
    __ram=0
    __internal=0
    def setModel(self,mod=""):
        self.__model=mod
    def getModel(self):
        return self.__model
    def setPrice(self,pri=""):
        self.__Price=pri
    def getPrice(self):
        return self.__Price
    def setRam(self,ra=""):
        self.__ram=ra
    def getRam(self):
        return self.__ram
    def setInternal(self,inte=""):
        self.__internal=inte
    def getInternal(self):
        return self.__internal                
M=Mobile()
M.setModel("Iphone")
M.setPrice(690000.0)
M.setRam(128)
M.setInternal(128)
print(M.getModel(),M.getPrice(),M.getRam(),M.getInternal())