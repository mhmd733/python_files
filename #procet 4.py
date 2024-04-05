#procet 4
import random
max_attempts = 5
def The_user_inp(): 
    while True:
        user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
        if user_input == 'q':
          return None  # Indicate the wish to quit
        if user_input in ["rock", "paper", "scissors"]: 
            return user_input
        else:
            print("Invalid input. Please try again.")

def Check(user_input, cupmuter_choes):
    if user_input == cupmuter_choes:
        return "tie"
    elif (user_input == "rock" and cupmuter_choes == "scissors") or \
         (user_input== "paper" and cupmuter_choes== "rock") or \
         (user_input== "scissors" and cupmuter_choes== "paper"):
        return "you won" 
    else:
        return "the cumputer won"

def Play_The_Game():
    user_win = 0
    cumputer_win = 0
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        cupmuter_guess = random.randint(0, 2)
        cupmuter_choes = ["rock", "paper", "scissors"][cupmuter_guess]

        user_input = The_user_inp()
        if user_input is None:  # Check if the user wanted to quit
            break

        result = Check(user_input, cupmuter_choes)
        print(result) 

        if result == "you won":
            user_win += 1
        elif result == "the cumputer won":  # Correct spelling
            cumputer_win += 1

    print(f"Final Results: You won {user_win} times and the computer won {cumputer_win} times")

# Start the game
Play_The_Game()
