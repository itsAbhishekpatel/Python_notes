bid = {

}

flag = True

while flag:
    name = input("What is your name?:")
    price =int(input("What's your bid?:"))

    bid[name] = price

    state = input("Are there any other bidder? Type 'yes' or 'no'.")
    if state == "no":
        flag = False

price = list(bid.values())
price.sort()

highest_bid = price[len(price)-1]


print(f"The winer is {bid.keys()[bid.values().index(highest_bid)]} with a bid price of $ {highest_bid}")

