import random
from turtle import *
hideturtle()

speed(0)

def hit_stand_dd_cmd(x,y,card_num):
    global hit_stand_dd
    global deposit
    global round
    global double_down
    
    if double_down == True:
        hit_stand_dd = raw_input("What do you want to do? (hit, stand, double down): ")
    else:
        hit_stand_dd = raw_input("What do you want to do? (hit, stand): ")
    if hit_stand_dd == 'hit':
        double_down = False
        if card_num == player_five_num or card_num == player_six_num:
            begin_fill()
            color('white')
            card_outline(x,y)
            end_fill()
            color('black')
            player_card(x,y,card_num)
        else:
            player_card(x,y,card_num)
    elif hit_stand_dd == 'stand':
        dealer_ai()
    elif hit_stand_dd == 'double down':
        if double_down == True:
            if round > deposit:
                print "Insufficient funds"
                print 'Your balance: $' + str(deposit)
                hit_stand_dd_cmd(x,y,card_num)
            
            elif card_num == player_five_num or card_num == player_six_num:
                begin_fill()
                color('white')
                card_outline(x,y)
                end_fill()
                color('black')
                player_card(x,y,card_num)
                deposit = deposit - round
                round = round*2
                dealer_ai()
                
            else:
                player_card(x,y,card_num)
                deposit = deposit - round
                round = round*2
                dealer_ai()
        else:
            print 'invalid command'
            hit_stand_dd_cmd(x,y,card_num)
    else:
        print 'invalid command'
        hit_stand_dd_cmd(x,y,card_num)

def card_outline(x,y):
    penup()
    setposition(x,y)
    pendown()
    for i in range (2):
        forward(75)
        left(90)
        forward(100)
        left(90)
#empty first dealer card
def card_empty(x,y):
    card_outline(x,y)
    left(53.13)
    forward(125)
    left(126.87)
    forward(75)
    left(126.87)
    forward(125)
    left(53.13)
    penup()
#moves turtle out of the view
def tclear():
    penup()
    setposition(-200,-200)
def clear_table():
    color('white')
    begin_fill()
    for i in range(4):
        forward(400)
        left(90)
    end_fill()
    color('black')

def two(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    for i in range(2):
        forward(10)
        right(90)
    for i in range(2):
        forward(10)
        left(90)
    forward(10)
def three(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    for i in range(2):
        forward(10)
        right(90)
    forward(10)
    backward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(180)
def four(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    right(90)
    forward(10)
    left(90)
    forward(10)
    backward(5)
    left(90)
    forward(10)
    backward(20)
    right(90)
def five(x,y):
    card_outline(x,y)
    penup()
    setposition(x+20,y+90)
    pendown()
    left(180)
    for i in range(2):
        forward(10)
        left(90)
    for i in range(2):
        forward(10)
        right(90)
    forward(10)
    right(180)
def six(x,y):
    card_outline(x,y)
    penup()
    setposition(x+20,y+90)
    pendown()
    left(180)
    forward(10)
    left(90)
    forward(20)
    for i in range(3):
        left(90)
        forward(10)
    right(180)
def seven(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    forward(10)
    right(90)
    forward(20)
    left(90)
def eight(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    for i in range(6):
        forward(10)
        right(90)
    left(90)
    for i in range(3):
        forward(10)
        right(90)
def nine(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    for i in range(5):
        forward(10)
        right(90)
    forward(20)
    left(90)
def ten(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    right(90)
    forward(20)
    penup()
    setposition(x+15,y+90)
    pendown()
    left(180)
    for i in range(2):
        right(90)
        forward(10)
        right(90)
        forward(20)
    right(90)
def jack(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    forward(15)
    backward(5)
    right(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
def queen(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    for i in range(3):
        forward(10)
        right(90)
        forward(20)
        right(90)
    forward(5)
    left(90)
    backward(5)
    forward(5)
    for i in range(2):
        forward(5)
        left(90)
    right(90)
def king(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    right(90)
    forward(20)
    backward(10)
    left(135)
    forward(14.14)
    backward(14.14)
    right(90)
    forward(14.14)
    backward(14.14)
    left(45)
def ace(x,y):
    card_outline(x,y)
    penup()
    setposition(x+10,y+90)
    pendown()
    right(90)
    forward(20)
    backward(20)
    left(90)
    for i in range(5):
        forward(10)
        right(90)
    forward(20)
    left(90)

def club(x,y):
    penup()
    setposition(x+32.5,y+30)
    pendown()
    begin_fill()
    forward(10)
    left(90)
    forward(10)
    right(135)
    for i in range(2):
        circle(7.5,320)
        right(255)
    circle(7.5,320)
    right(135)
    forward(5)
    end_fill()
    left(90)
def diamond(x,y):
    penup()
    setposition(x+37.5,y+30)
    pendown()
    color("red")
    begin_fill()
    left(62.5)
    forward(20)
    left(55)
    forward(20)
    left(125)
    forward(20)
    end_fill()
    left(117.5)
    color("black")
def heart(x,y):
    penup()
    setposition(x+37.5,y+30)
    pendown()
    color("red")
    begin_fill()
    left(45)
    forward(22.5)
    left(45)
    circle(7.5,180)
    left(180)
    circle(7.5,180)
    end_fill()
    left(90)
    color("black")
def spade(x,y):
    penup()
    setposition(x+32.5,y+30)
    pendown()
    begin_fill()
    forward(10)
    left(90)
    forward(10)
    right(135)
    circle(5,180)
    forward(20)
    left(90)
    forward(20)
    circle(5,180)
    right(135)
    forward(10.15)
    left(90)
    forward(5)
    end_fill()
    

suits = [club,diamond,heart,spade]
cards_num = ("2","3","4","5","6","7","8","9","10","10","10","10","11")
ten_card = [ten, jack, queen, king]

#draws player card and adds to player total
def player_card(x,y,card_num):
    global player_total
    if card_num == '2':
        two(x,y)
        player_total = player_total + 2
    elif card_num == '3':
        three(x,y)
        player_total = player_total + 3
    elif card_num == '4':
        four(x,y)
        player_total = player_total + 4
    elif card_num == '5':
        five(x,y)
        player_total = player_total + 5
    elif card_num == '6':
        six(x,y)
        player_total = player_total + 6
    elif card_num == '7':
        seven(x,y)
        player_total = player_total + 7
    elif card_num == '8':
        eight(x,y)
        player_total = player_total + 8
    elif card_num == '9':
        nine(x,y)
        player_total = player_total + 9
    elif card_num == '10':
        ten_card_rand(x,y)
        player_total = player_total + 10
    elif card_num == '11':
        ace(x,y)
        player_total = player_total + 11
    random.choice(suits)(x,y)

def dealer_one_empty():
    card_empty(-150,50)
def dealer_one_clear():
    for i in range(8):
        color("white")
        card_empty(-150,50)
    color("black")

#draws dealer card and adds to dealer's total
def dealer_card(x,y,card_num):
    global dealer_total
    if card_num == '2':
        two(x,y)
        dealer_total = dealer_total + 2
    elif card_num == '3':
        three(x,y)
        dealer_total = dealer_total + 3
    elif card_num == '4':
        four(x,y)
        dealer_total = dealer_total + 4
    elif card_num == '5':
        five(x,y)
        dealer_total = dealer_total + 5
    elif card_num == '6':
        six(x,y)
        dealer_total = dealer_total + 6
    elif card_num == '7':
        seven(x,y)
        dealer_total = dealer_total + 7
    elif card_num == '8':
        eight(x,y)
        dealer_total = dealer_total + 8
    elif card_num == '9':
        nine(x,y)
        dealer_total = dealer_total + 9
    elif card_num == '10':
        ten_card_rand(x,y)
        dealer_total = dealer_total + 10
    elif card_num == '11':
        ace(x,y)
        dealer_total = dealer_total + 11
    random.choice(suits)(x,y)

deposit = float(raw_input('How much money do you want to deposit? '))

def dealer_check():
    global deposit
    global dealer_total
    global player_total
    global dealer_soft
    
    tclear()
    print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
    if dealer_total > 21:
            print 'You win'
            deposit = deposit + round*2
            print 'Your balance: $' + str(deposit)
    elif player_total > 21:
            print "Bust! You lose"
            print 'Your balance: $' + str(deposit)
    elif dealer_total == player_total:
        print 'Its a draw!'
        deposit = deposit + round
        print 'Your balance: $' + str(deposit)
    elif dealer_total == 21:
        print 'You lose'
        print 'Your balance: $' + str(deposit)
    
    elif dealer_total < 21 and dealer_total > player_total:
        print 'You lose'
        print 'Your balance: $' + str(deposit)
    elif dealer_total < 21 and dealer_total < player_total:
        print 'You win'
        deposit = deposit + round*2
        print 'Your balance: $' + str(deposit)
        
        
def dealer_ai():
    global deposit
    global dealer_total
    global player_total
    global dealer_soft

    dealer_one_clear()
    dealer_card(-150,50,dealer_one_num)
    if dealer_one_num == '11':
        dealer_soft = True
    if dealer_total >= 17:
        if dealer_soft == True and dealer_total > 21:
            dealer_total = dealer_total - 20
            dealer_soft = False
            dealer_card(10,50,dealer_three_num)
        else:
            dealer_check()
            return
    else:
        dealer_card(10,50,dealer_three_num)
        if dealer_three_num == '11':
            dealer_soft = True
        
    if dealer_total >= 17:
        if dealer_total > 21 and dealer_soft == True:
            dealer_total = dealer_total - 10
            dealer_soft = False
            if dealer_total <= 17:
                dealer_card(90,50,dealer_four_num)
        else:
            dealer_check()
            return 
    else:
        dealer_card(90,50,dealer_four_num)
        if dealer_four_num == '11':
            dealer_soft = True
    
    if dealer_total >= 17:
        if dealer_total > 21 and dealer_soft == True:
            dealer_total = dealer_total - 10
            dealer_soft = False
            if dealer_total <= 17:
                color('white')
                begin_fill()
                card_outline(-125,13)
                end_fill()
                color('black')
                dealer_card(-125,13,dealer_five_num)
                if dealer_five_num == '11':
                    dealer_soft = True
        else:
            dealer_check()
            return 
    else:
        color('white')
        begin_fill()
        card_outline(-125,13)
        end_fill()
        color('black')
        dealer_card(-125,13,dealer_five_num)
        if dealer_five_num == '11':
            dealer_soft = True

    if dealer_total >= 17:
        if dealer_total > 21 and dealer_soft == True:
            dealer_total = dealer_total - 10
            dealer_soft = False
            if dealer_total <= 17:
                color('white')
                begin_fill()
                card_outline(-45,13)
                end_fill()
                color('black')
                dealer_card(-45,13,dealer_six_num)
                if dealer_six_num == '11':
                    dealer_soft = True
        else:
            dealer_check()
            return 
    else:
        color('white')
        begin_fill()
        card_outline(-45,13)
        end_fill()
        color('black')
        dealer_card(-45,13,dealer_six_num)
        if dealer_six_num == '11':
            dealer_soft = True
    
    if dealer_total >= 17:
        if dealer_total > 21 and dealer_soft == True:
            dealer_total = dealer_total - 10
            dealer_soft = False
            dealer_check()
            return
        else:
            dealer_check()
            return

while True:
    player_total = 0
    dealer_total = 0
    soft = False
    dealer_soft = False
    double_down = True
    
    ten_card_rand = random.choice(ten_card)

    player_one_num = random.choice(cards_num)
    player_two_num = random.choice(cards_num)
    player_three_num = random.choice(cards_num)
    player_four_num = random.choice(cards_num)
    player_five_num = random.choice(cards_num)
    player_six_num = random.choice(cards_num)
    
    dealer_one_num = random.choice(cards_num)
    dealer_two_num = random.choice(cards_num)
    dealer_three_num = random.choice(cards_num)
    dealer_four_num = random.choice(cards_num)
    dealer_five_num = random.choice(cards_num)
    dealer_six_num = random.choice(cards_num)
    
    if deposit == 0:
        print 'You are bankrupt. Please run the game again.'
        break
    round = float(raw_input('How much do you want to bet? '))

    if round > deposit:
        print "Insufficient funds"
        print 'Your balance: $' + str(deposit)
        continue
    
    tclear()
    clear_table()
    
    deposit = deposit - round
    print 'Your balance: $' + str(deposit)
    
    #first two dealer cards (1 empty, 1 not)
    dealer_one_empty()
    dealer_card(-70,50,dealer_two_num)
    if dealer_two_num == '11':
        dealer_soft = True
    
    #first two player cards when game starts
    player_card(-150,-150,player_one_num)
    player_card(-70,-150,player_two_num)
    
    
    if player_one_num == '11' or player_two_num == '11':
        soft = True
        if soft == True and player_total > 21:
            player_total = player_total - 20
            soft = False
            if dealer_soft == True:
                print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total) + ' soft'
            else:
                print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        elif dealer_soft == True:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total) + ' soft'
        else:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total)
    elif dealer_soft == True:
        print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total) + ' soft'
    else:
        print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
    tclear()
    
    if player_total == 21:
        print "Blackjack, You Win!"
        deposit = deposit + round*1.5
        print 'Your balance: $' + str(deposit)
        continue
    #card 3 player
    else:
        hit_stand_dd_cmd(10,-150,player_three_num)
    if hit_stand_dd == 'stand' or hit_stand_dd == 'double down':
        continue
    else:
        tclear()
        if player_three_num == '11':
            soft = True
        if soft == True and player_total > 21:
            player_total = player_total - 10
            soft = False
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        elif soft == True and player_total < 21:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total)
        else:
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        if player_total == 21:
            print "You win!"
            deposit = deposit + round*2
            print 'Your balance: $' + str(deposit)
            continue
        elif player_total > 21:
            print "Bust! You lose"
            print 'Your balance: $' + str(deposit)
            continue
        else:
            hit_stand_dd_cmd(90,-150,player_four_num)
    if hit_stand_dd == 'stand':
        continue
    else:
        tclear()
        if player_four_num == '11':
            soft = True
        if soft == True and player_total > 21:
            player_total = player_total - 10
            soft = False
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        elif soft == True and player_total < 21:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total)
        else:
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        
        if player_total == 21:
            print "You win!"
            deposit = deposit + round*2
            print 'Your balance: $' + str(deposit)
            continue
        elif player_total > 21:
            print "Bust! You lose"
            print 'Your balance: $' + str(deposit)
            continue
        else:
            hit_stand_dd_cmd(-125,-187,player_five_num)
    if hit_stand_dd == 'stand' or hit_stand_dd == 'double down':
        continue
    else:
        tclear()
        if player_five_num == '11':
            soft = True
        if soft == True and player_total > 21:
            player_total = player_total - 10
            soft = False
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        elif soft == True and player_total < 21:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total)
        else:
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        
        if player_total == 21:
            print "You win!"
            deposit = deposit + round*2
            print 'Your balance: $' + str(deposit)
            continue
        elif player_total > 21:
            print "Bust! You lose"
            print 'Your balance: $' + str(deposit)
            continue
        else:
            hit_stand_dd_cmd(-45,-187,player_six_num)
    if hit_stand_dd == 'stand' or hit_stand_dd == 'double down':
        continue
    else:
        tclear()
        if player_six_num == '11':
            soft = True
        if soft == True and player_total > 21:
            player_total = player_total - 10
            soft = False
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
        elif soft == True and player_total < 21:
            print "Your Total: " + str(player_total) + ' soft,' + "  Dealer's Total: " + str(dealer_total)
        else:
            print "Your Total: " + str(player_total) + "      Dealer's Total: " + str(dealer_total)
    
    if player_total == 21:
        print "You win!"
        deposit = deposit + round*2
        print 'Your balance: $' + str(deposit)
        continue
    elif player_total < 21:
        print "You win!"
        deposit = deposit + round*2
        print 'Your balance: $' + str(deposit)
        continue
    elif player_total > 21:
        print "Bust! You lose"
        print 'Your balance: $' + str(deposit)
        continue

print 'Gameover'
