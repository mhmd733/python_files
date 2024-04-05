# main.py
import random
lower_bound = 1
upper_bound = 1000
max_attempts = 10
secret_number = random.randint(lower_bound,upper_bound)
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound} : "))
            if lower_bound <= guess <= upper_bound:
              return guess
            else : 
              print ("invalid input. please enter a numder within the specified range. ")
        except ValueError:
           print(" invalid input. please enter a valid number")
def check_guess(guess,secret_number):
   if guess == secret_number:
      return "correct"
   elif guess < secret_number:
      return "too low"
   else :
        return "too high"
def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts : 
        attempts += 1
        guess = get_guess()
        result = check_guess(guess,secret_number)
        if result == "correct"    :
          print(f"congratulation! You guessed the correct number {secret_number} in {attempts} attempts")
          won = True
          break 
        else :
          print(f"{result}. try again")
    if not won :
      print(f"sorry, you ran out of attempt! The secret numder was {secret_number}. ")  

if __name__ == "__main__":
   print("Welllcome To The Number Guessing Game!")
   play_game()
