# number guessing 
tryes = 0
gess = input("Enter a gess : ") 
the_right_answer = "moo"
tryes_limit = 3
def right_answer() :
 while gess != the_right_answer:
 
  if gess != the_right_answer and tryes < tryes_limit:
   tryes = 1
   tryes += 1
  return
 if gess == the_right_answer or tryes > tryes_limit  :
  print("good job")

print( right_answer())