def calculate_the_volume_of_a_box(height, length, width):
    try:
        volume = int(height) * int(length) * int(width)
        return volume
    except ValueError:
        print("Error: Please enter only numbers for dimensions.")
        return None  # Indicate that the calculation failed

height = input("What is the height? :")
length = input("What is the length? :")
width = input("What is the width? :")

result = calculate_the_volume_of_a_box(height, length, width)
print("The volume of the box is:", result)
if result is not None:
    
    print("The volume of the box is:", result)
