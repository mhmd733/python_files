# __main__
import random
lower_bound = 1
upper_bound = 500
max_attempts = 10
secret_number= random.randint(lower_bound,upper_bound)
def guess_game():
    while True:
        try :
         guess = int(input(f"Enter your gues between {lower_bound} and {upper_bound} : "))
         if   upper_bound > guess > lower_bound :
            return  guess
         else :
            print(f"The number must br between {lower_bound} and {upper_bound} ")
        except ValueError:
           print(" The guess must be a number ")
def test_(guess,secret_number):
         if guess == secret_number :
          return "correct"
         elif guess > secret_number:
           return "too high" 
         elif guess < secret_number:
            return "too low"
def play_the_game():
    attempts = 0
    won = False
    while  attempts < max_attempts :
       attempts += 1
       guess =  guess_game()
       result = test_(guess,secret_number)
       if result == "correct":
          print("nice job")
          won = True
          break
       else:
          print(f"{result} try again")
    if not won:
       print(f"you ran out of attempts the number was {secret_number} ")
if __name__== "__main__":
   print("Wellcome to the game")
   play_the_game()
       
