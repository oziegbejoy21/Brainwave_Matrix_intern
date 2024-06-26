#password strength checker program
import re 
#password must be at least 8 charcter long
password=input("Enter your password:")
if len(password)< 8:
    print("password must be at least 8 character long.")
    #password must contain at least one uppercase letter.
elif not re.search("[A-Z]",password):
    print("password must contain at least one uppercase letter.")
    #password must contain at least one lowercase letter.
elif not re.search("[a-z]",password):
     print("password must contain at least one lowercase letter.")
    #password must contain at least one number.
elif not re.search("[0-9]",password ):
    print("password must contain at least one number.")
    #password must contain at least one symbol.
elif not re.search("[!-*]",password):
     print("password must contain at least one symbol.")
else:
    print("password is strong")



