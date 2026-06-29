print("Bidding Program!")

auction = {}

while True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    auction[name] = price

    continue_bidding = input("Add another bidder? (yes/no): ").lower()
    if continue_bidding != "yes":
        break
    print("\n" * 100)

winner = max(auction, key=auction.get)

print("\n" * 100)
print(f"The winner is {winner} with a bid of ${auction[winner]}")