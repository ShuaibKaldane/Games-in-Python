import random
word = ["cat" , "pen" , "dog"]
final_word = random.choice(word)
display = ["_"]*len(final_word)
print(final_word)
guessed_letters = []
lives = 4
while  lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Lives left:", lives)
    user_input = input("Enter a letter: ").lower()
    if user_input in guessed_letters:
        print("You already guessed this letter!")
        continue
    guessed_letters.append(user_input)
    if user_input in final_word:
        for i in range(len(final_word)):
            if final_word[i] == user_input:
                display[i] = user_input
        print("Correct guess!")
    else:
        lives -= 1
        print("Wrong guess!")

if "_" not in display:
    print("\n You won the game!")
    print("The word was:", final_word)
else:
    print("\n😢 You lost!")
    print("The word was:", final_word)

  
