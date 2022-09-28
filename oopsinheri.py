# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).
"""
class Profile:
  def __init__(self):
    self.name = 'deepak' 
    self.email = 'deepak@gmail.com'
    self.age= 22
profile = Profile()
print(profile.name)
"""


# 2. Write a python script to update the above Profile class with encapsulation.
"""
class Profile:
  def __init__(self):
    self.name = 'deepak' 
    self.email = 'deepak@gmail.com'
    self.age= 22

  def getAgeName(self):
    print(self.age)
    print(self.name)
  
  def setAgeName(self,age,name):
    self.age = age
    self.name = name

profile = Profile()
profile.setAgeName(23, 'Deepak Kumar Nayak')
profile.getAgeName()
"""

# 3. Write a python script to update 2nd Question, change email and age to __email and
# __age.
"""
class Profile:
  def __init__(self):
    self.name = 'deepak' 
    self.__email = 'deepak@gmail.com'
    self.__age= 22

  def getAgeName(self):
    print(self.age)
    print(self.name)
  
  def setAgeName(self,age,name):
    self.__age = age
    self.__name = name

profile = Profile()
profile.getAgeName()
"""
# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.
"""
class Profile:
  platform = "Ineuron"
  def __init__(self):
    self.name = 'deepak' 
    self.__email = 'deepak@gmail.com'
    self.__age= 22

  def getAgeName(self):
    print(self.age)
    print(self.name)
  
  def setAgeName(self,age,name):
    self.__age = age
    self.__name = name

  @classmethod
  def getPlatformname(cls):
    print(cls.platform)

profile = Profile()
profile.getPlatformname()
"""
# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.

class Calculator:
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
  
  def __add__(self,other):
    totalOne = self.m1 + other.m1
    totalTwo = self.m2 + other.m2
    add = Calculator(totalOne,totalTwo)
    return add

  def __sub__(self,other):
    totalOne = self.m1- other.m1
    totalTwo = self.m2 - other.m2
    sub = Calculator(totalOne,totalTwo)
    return sub

  def __str__(self):
    return str(self.m1)+ " : " + str(self.m2)


calculatorOne = Calculator(90,70)
calculatorTwo = Calculator(10,60)

add = calculatorOne + calculatorTwo
sub = calculatorOne - calculatorTwo
print(add)
print(sub)



# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.


class Calculator2_0(Calculator):
  def __init__(self,m1,m2):
    super().__init__(m1,m2)

  def __mul__(self,other):
    totalOne = self.m1 * other.m1
    totalTwo = self.m2 * other.m2
    product = Calculator2_0(totalOne,totalTwo)
    return product

  def __truediv__(self,other):
    totalOne = self.m1 / other.m1
    totalTwo = self.m2 / other.m2
    divisionresult = Calculator2_0(totalOne,totalTwo)
    return divisionresult


calculatorOne = Calculator2_0(90,70)
calculatorTwo = Calculator2_0(10,60)

product = calculatorOne * calculatorTwo
divisonresult = calculatorOne / calculatorTwo
print(product)
print(divisonresult) 



# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).


class Phone:
  def calling(self):
    print('calling')

  def sms(self):
    print('sms')

phone = Phone()




# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.

class SmartPhone(Calculator2_0,Phone):
  pass
smartphone = SmartPhone(10,20)
# smartphone.calling()


# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).

class TrueCaller:
  def __init__(self,name,number):
    self.name = name
    self.numbers = number
  
  def fetchName(self,name,number):
    self.name = name 
    self.number = number
    dict= {}
    dict[self.name]=self.number
    for key, value in dict.items():
      if value == self.number:
          print(key)

  def getName(self):
    print(self.name)

  def addNewEntry(self,name,number):
    self.name = name
    self.number=number


  
truecaller = TrueCaller('deepak',8908757968)
# truecaller.fetchName('rahul',8908757968)
truecaller.addNewEntry('Deepak Kumar',7205689584)
# truecaller.getName()




# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.

class Smartphone(Calculator2_0,Phone):
  def getFetchMethod(self,trueclr):
    trueclr.fetchName(self,'Alex',7890876564)

a=Smartphone(10,20)
a.getFetchMethod(TrueCaller)