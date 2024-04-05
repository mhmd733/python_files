# if 
def he_is_a_man():
    print("cool")
def he_is_not_a_man():
    print("women haaa")
result = input(" are you a male (true or false) :")
is_male = result.lower() == "true"
if is_male : 
   he_is_a_man()
else:
   he_is_not_a_man()
def calculate_area(width, height):
    area = int(width) * int(height)
    print(" the area is " + str(area))
width = input(" what is the width :")
height = input("What is that height :")
calculate_area(width, height)

