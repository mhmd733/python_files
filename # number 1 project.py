# number 1 project



print("Wekkcome to my game : ")

playing = input("Do you want to play the game? : ")
if playing.lower() == "yes" :
    print("okey ")
else :
    print('soo sad, see you next time :')
    quit()

def The_Game():
 max_attempts = 1
 attempts= 0
 result = 0
 while attempts < max_attempts :
     attempts += 1
     answer1 =input("what does cpu stand for? :")
     if answer1.lower() == "central procssing unit" :
        result += 1
        print(" that was right")
     else :
        print("wrong answer :(")

     answer2 =input("where i have been born ? :")
     if answer2.lower() == "omdurman" :
        result += 1
    
        print(" soo you do do know me :)")
     else :
        print(" wrong answer :(")


     answer3 =input("what is my first nickname ? :")
     if answer3.lower() == "spidy" :
        result += 1
        print("I geuss you are one of my best frinds ")
     else :
        print("wrong answer :(")

     answer4 =input("who am I? :")
     if answer4.lower() == "a king" :
        result += 1
        print(" that was right")
     else :
     
       print("wrong answer :(")    
    
 
     if result == 1 or 2:
        print(f'you gut lucky you answered {result} right')
     elif result == 3 or 4 :
        print(f'good,nice you gut {result} right')
 
The_Game()
