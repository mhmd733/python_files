# project 5
def Check():
        try :
            user_name = int(input("What is your name : "))
            if user_name == int :
                print('please enter a name')
    
        except ValueError:
            return user_name
        

            
def The_game():
    user_name = Check()
    chose1 = input(f"Do you want to go lift or right {user_name} : ").lower()
    if chose1 == "right" :
        print("The was a amn need your help")
The_game()