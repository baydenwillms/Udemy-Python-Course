logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Silent Auction.")
auction = {}

def new_bidder():
    name = input("Please enter your name:\n> ")
    bid = input("What is your bid?\n> $")
    bid = int(bid)
    auction[name] = bid

new_bidder()
auction_finished = False
while auction_finished == False:

    add_bidder = input("Are there any other bidders? (Enter Yes or No)\n> ").lower()
    if add_bidder == "no":
        current_highest_bid = 0
        for name in auction:
            if auction[name] > current_highest_bid:
                current_highest_bid = auction[name]
        
        auction_finished = True
        print("The Silent Auction has closed.")
    if add_bidder == "yes":
        new_bidder()

for name in auction:
    if auction[name] == current_highest_bid:
        winner = name

print(f"The winner is {winner}, with a bid of ${current_highest_bid}.")


