# tranlater
phrase = input("Enter a phare :")
def translate(phrase):
    translation = ""
    for letter in phrase :
     if letter in "Aa":
       translation = translation + "s"
     elif letter in "Bb" :
       translation = translation + "j"
     elif letter in "Cc" :
       translation = translation + "v"
     elif letter in "Dd":
       translation= translation + "p"
     elif letter in "Ee":
       translation = translation + "h"
     elif letter in "Ff": 
       translation = translation + "z"
     elif letter in "Gg": 
       translation = translation + "q"
     elif letter in "Hh":
       translation = translation + "f" 
     elif letter in "Ii" :
       translation =translation + "n"
     elif letter in "Jj"  :
       translation = translation + "b"
     elif letter in "Kk"   :
       translation = translation +"u"
     elif letter in "Ll" :
       translation = translation + "a"
     elif letter in "Nn":
       translation = translation + "l"
     elif letter in "Mm": 
       translation = translation+ "d"
     elif letter in "Oo":
       translation = translation +"w"
     elif letter in "Pp":
       translation = translation ="x"
     elif letter in "Qq":
       translation = translation + "e"
     elif letter in "Rr":
       translation = translation + "i"
     elif letter in "Ss" :
       translation = translation +"m"
     elif letter in "Tt": 
       translation = translation + "k"
     elif letter in "Uu":
       translation = translation +  "o"
     elif letter in "Vv":
       translation = translation + "r"
     elif letter in "Ww":
       translation = translation + "c"
     elif letter in "Xx":
       translation = translation + "t"
     elif letter in "Yy":
       translation = translation + "g"  
     elif letter in "Zz" :
       translation = translation + "y"
     else:
       translation = translation + " "
    return translation   
result = translate(phrase)    
print(result)
