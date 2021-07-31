from art import logo

print(logo)
print("Welcome to the secret auction program")

bidders = []
response = "yes"


def add_bidder(bidder_name, bidder_bid):
    new_bidder = {"name": bidder_name, "bid": bidder_bid}
    bidders.append(new_bidder)


def request_bidder_info():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    add_bidder(name, bid)


def determine_winner():
    highest_bidder = {"name": "None", "bid": 0}
    for bidder in bidders:
        if int(bidder["bid"]) > int(highest_bidder["bid"]):
            highest_bidder = bidder
    return highest_bidder


while response == "yes":
    request_bidder_info()
    response = input("Are there any other bidders? Type 'yes' or 'no'.")
    print('\n'*80)


highest_bidder = determine_winner()
print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}.")