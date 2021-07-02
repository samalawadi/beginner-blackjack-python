# beginner-blackjack-python

# Basics
You must try to get your cards as close to 21 as possible, without going over 21. 
You win if your cards are equal to or below 21, but more than the dealer.

Aces can be valued at either 11 or 1.
A blackjack is when you get 21 from the first two cards (from an A and a 10)

**Commands**
1) hit: asking for another card to get closer to 21
2) stand: not asking for another card
3) double down: doubling your initial bet to recieve another card (you can't hit after 
this). Doubling your initial bet means you'll also get double returns if you win. Only
availble before hitting.

**Pay**
You will get 2:1 pay out. Meaning if you bet $100 and win, you will get $200 back.
If you get a blackjack, the pay out will be 1.5:1
You get your money back if you draw with the dealer

# Specific Rules
6 card charlie is implemented (automatically win if you have 6 cards without
busting (going over 21)). Insurance (betting on dealer w/ ace) and spliting is not 
allowed.
"""
