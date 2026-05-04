def Auction():
    data = {}
    highest_bid = 0
    winner = ""
    while True:
        name = input("Enter the bidder name\n")
        value = int(input("Enter the ammount $ \n"))
        data[name] = value
        another = input("Is there any another bidder Yes or no\n").lower()
        if (another == "no"):
            break
    print(f'The biders are {data}')
    for element in data :
        if (data[element] >highest_bid):
            highest_bid = data[element]
            winner = element
    print(f"The highest bidder name is {winner} and the ammount is $ {highest_bid}")

Auction()