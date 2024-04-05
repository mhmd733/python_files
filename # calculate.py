# calculate 
def calculate_the_volume_of_a_box (height, length, width):
    volume = int(height)*int(length)*int(width)
    return volume
height = input("What is the height :")
length = input("What is the length :")
width = input("What is the width :")
result = calculate_the_volume_of_a_box( height, length, width) 
print(result)