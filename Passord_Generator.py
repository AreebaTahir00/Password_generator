import string
import random

def check_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_special = any(char in string.punctuation for char in password)
    if has_digit and has_letter and has_special:  
        return True
    

name=input("Enter your Name:")
for _ in range(4):
    num=input("Enter your Phone number:")
    if(len(num) == 11 and num.isdigit()):
         break
    print("TRY AGAIN")
    
for _ in range(3):
    email = input("Enter your Email id: ")
    if email.endswith("@gmail.com"):
        break
    print("Please enter a valid Gmail address (must end with '@gmail.com')")
else:
    Name=name.lower()
    Email= Name.replace(" ", "")
    email = Email+"@gmail.com"
    print("Too many invalid attempts. Using default email:",email)
    
    

password=input("Enter account password:")
passwrd = password

if check_password(passwrd):
    print("✅ ")
else:
    print("❌ ")
    word=input("Suggest Strong Password(Enter 'yes'):")
    if(word == "yes"):
        characters = string.ascii_letters + string.digits + string.punctuation
        passwrd = ''.join(random.choice(characters) for _ in range(12))
        if check_password(passwrd):
             pass
        else:
            print("Error occured") 

print("\nYour account is created successfully. :)")

print("\n\n ___________YOUR ACCOUNT INFORMATION__________")
print("Your name:",name,"\nYour contact :",num,"\nYour email id: ",email,"\nYour password: ",passwrd)

