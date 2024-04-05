# kl
#monthes ={}
my_birthday_date = "19/06/2003"
tryes = ""
tryes_count = 0
tryes_limit = 3
out_of_tryes = False
while tryes != my_birthday_date and not(out_of_tryes):
    if tryes_count < tryes_limit :
        tryes = input("do you know my birthday :")
        tryes_count += 1
    else :
        out_of_tryes = True

if out_of_tryes:
    print("I donot think you know me ")
else :
    print("cool")

