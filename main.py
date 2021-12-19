import os
import art


def bid_adder(name, bid):
    bids[name] = bid


def winner_finder(dict_of_bids):
    winner, maxbid = 0, 0
    print(dict_of_bids)
    for name in dict_of_bids:

        if dict_of_bids[name] > maxbid:
            maxbid = dict_of_bids[name]
            winner = name
    return f"{winner} won with {maxbid}$ bid"


bids = {}
name = ""
bid = 0
more_available_bidders = True


while more_available_bidders:
    name = input("what is your name \n>")
    bid = int(input("what is your bid\n>"))
    bid_adder(name, bid)
    if((input("are there any more bidders\n'y' or yes\n>") != "y")):
        more_available_bidders = False

print(winner_finder(bids))
