# procet 3.1
import random

from oscrypto import use_winlegacy
max_attempts = 3
cupmuter_guess = random.randint(0,2)
opstions = ["rock","paper","scissors"]
cupmuter_choes =opstions[cupmuter_guess]

  
        

def The_user_inp(): 
    while True:
        user_input = str(input("type rock/paper/scissors or Q to quit." ).lower())
        if user_input in opstions : 
            return user_input
        else:
            break
def Check(user_input,cupmuter_choes):
 if user_input == cupmuter_choes:
    return("tie")
 elif user_input == "rock" and cupmuter_choes == "scissor" or user_input== "paper" and cupmuter_choes== "rock" or user_input== "scissors" and cupmuter_choes== "paper"  :
    return "you won" 
 else :
    return "the cumputer won"

def Play_The_Game():
    user_win= 0
    cumputer_win = 0
    attempts = 0
    won = False
    while attempts < max_attempts and user_win>2:
        attempts+=1
        result = Check(user_input,cupmuter_choes)
        if result == "you won":
         user_win +=1
         print(f"you won {user_win} times")
        else :
            cumputer_win +=1
            print(f"the cumputer won {cumputer_win} times")
    
    
    print(f"you won {user_win} times and the cumputer won {cumputer_win} times")