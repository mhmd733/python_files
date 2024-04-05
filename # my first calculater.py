# my first calculater
try :
 num1 = float(input("Enter first number :"))
except ValueError :
 print("Invalid input")
try :
  op = input("Eneter an opareter :")
except NameError:
 print("Invalid input")
try :
    num2 = float(input("Enter secande numder :"))
except ValueError:
 print("Invalid input")

if op != "=,-,*,/":
 print("ivalid opareter")
elif op == "+" :
 print( num1+num2 ) 
elif op == "-" :
 print( num1-num2)
elif op == "*" :
 print( num1*num2 )
elif op == "/" :
 print(num1 / num2)
