def Auction():
    data = {}
    highest_bid = 0
    winner = ""
    while True:
        name = input("Enter the bidder name \n")
        ammount = int(input("Enter the ammount $ \n"))
        data[name]= ammount
        other = input("IS there any other bidder yes or no\n").lower()
        if(other == "no"):
            break
    print(f'Available Bidder are : {data}')
    for element in data:
     if(data[element] > highest_bid):
                highest_bid = data[element]
                winner = element
    print(f'Winner of this Bid is {winner} and the ammount is $ {highest_bid}')
Auction()