# classes
def hello ():
 print("shello")
print(type(hello))

string = "hello"
print(string.upper())


class Dog :
 
 def __init__(self,name,age):
  self.name = name
  self.age = age
  print(name)

 def Meow(self):
  return self.name
 

 
 def get_age(self):
  return self.age
d2 = Dog("Bill",32)
print(d2.get_age())
print(d2.Meow())




