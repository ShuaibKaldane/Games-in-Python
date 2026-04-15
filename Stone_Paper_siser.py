import random
# 0 - Rock
# 1 - Paper
# 2 - Sissers
rules = ["Rock" , "Paper" , "Sisers"]
name = input("Enter your name\n")
computer_choice = random.randint(0,2)
user = int (input("Enter 0 for Rock , 1 for paper , 2 for Sisers\n"))
if(computer_choice == user):
    print("Draw")
elif(computer_choice == 0 and user == 1):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print(f"you won {name}")
elif(computer_choice == 1 and user == 0):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print("Computer Won")
elif(computer_choice == 1 and user == 2):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print(f"you won {name}")
elif(computer_choice == 2 and user == 1):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print("Computer Won")
elif(computer_choice == 0 and user == 2):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print("Computer Won")
elif(computer_choice == 2 and user == 0):
    print(f"Computer Choice : {rules[computer_choice]}")
    print(f"User Choice : {rules[user]}")
    print(f"you won {name}")



