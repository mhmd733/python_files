#math problems
import time
import random
OPERATORS = ["+","-","*"]
min_opera = 3
max_opera = 12
TOTAL_PROBLEMS = 10
def Generate_problem():
   left = random.randint(min_opera,max_opera)
   right= random.randint(min_opera,max_opera)  
   operator = random.choice(OPERATORS)  
   expr = str(left) + " " + operator  + " "+str(right)
   answer = eval(expr)
   return expr, answer
wrong = 0
p=input("Press enter to start :")
if p == 0 :
  print("noooo")
else:
 
  
 print("---------------------")
 start_time = time.time()
 for i in range(TOTAL_PROBLEMS):
    expr,answer = Generate_problem()
    while True :
     guess = input("problem # " + str(i+1) + ":" + expr + " =")
     if guess == str(answer):
       break
end_time = time.time()
total_time= round(end_time-start_time)
print("---------------------") 
print(f"NICE WORK!, your time was {total_time} seconds!")   