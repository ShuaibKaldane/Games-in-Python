import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","\"","#","$","%","&","'","(",")","*","+",
           ",","-",".","/",";",":","<","=",">","?","@",
           "[","\\","]","^","_","`","{","|","}","~"]

print("Welcome to the Password Generator")
char = int(input("Enter the number of letters you want in Password\n"))
num = int(input("Enter the number how many number you want in the password\n"))
sym = int(input("Enter the number now many Symbols you need in your password\n"))

generated = ""

for i in range(0 , char):
    generated+=random.choice(letters)

for f in range (0, num):
    generated+= random.choice(numbers)

for g in range(0, sym):
    generated+= random.choice(symbols)

print(f"Your generated password is {generated}")