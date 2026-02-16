print("welcome to blind bid")
another_bid = "yes"
bids = {}
while another_bid == "yes":
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bids[name] = bid
    another_bid = input("Are there more people to make a bid: 'yes' or 'no': \n")
    if another_bid == "yes":
        print("\n" * 100)

winner = max(bids, key=bids.get)
highest_bid = bids[winner]
print(f"{winner} is the winner with a bid of ${highest_bid}")
