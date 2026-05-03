def ceapher():
    alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
 ]
    option1 = input("Type Encode for Encoding or Type decode for Decoding\n").lower()
    text = input("Enter your message\n")
    shift = int(input("How many number of shift you want:\n"))
    result = ""

    # decode = negative shift
    if option1 == "decode":
        shift = -shift

        for char in text:
            if char in alphabet:
                old_index = alphabet.index(char)
                new_index = (old_index + shift) % 26
                result += alphabet[new_index]
            else:
                result += char

    print("Result:", result)

ceapher()
