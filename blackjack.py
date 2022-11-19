#imports
import random
import tkinter
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import ttk

done = False
stay = False
bust = False

money = 100
bet = 5
amount = 0

# function for retrieving the images of the cards from device
def getCardImages(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    faceCards = ['jack', 'queen', 'king']

    ext= 'png'
    for suit in suits:
        # adding the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, ext)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))

        # adding the face cards
        for card in faceCards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, ext)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


def getCard(frame):
    # pop the card on the top of the deck
    next_card = deck.pop(0) 
    # and add it to the deck at the end
    deck.append(next_card)
    # show the image to a label 
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # return the card
    return next_card

# Function to calculate the total score of all cards in the list
def calcScore(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        # Ace is considered as 11 only once and rest of the time it is taken as 1 
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if its a bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


#Show the winner when the player stays
def staying():
    global done
    global stay
    global bust
    global money
    global amount
    stay = True
    dealer_score = calcScore(dealer_hand)
    player_score = calcScore(player_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(getCard(dealer_cardFrame))
        dealer_score = calcScore(dealer_hand)
        dealerScore.set(dealer_score)

    if player_score > 21 or dealer_score > player_score:
        winner.set("You lost...")
        done = True
        bust = True
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if dealer_score > 21 and player_score <= 21:
        winner.set("Dealer busted. You win!")
        done = True
        money += amount*2
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if dealer_score > 21 and player_score > 21:
        winner.set("You both busted... tie")
        done = True
        bust = True
        money += amount
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if dealer_score < player_score and player_score <= 21:
        winner.set("You win!")
        done = True
        money += amount*2
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if player_score == dealer_score:
        winner.set("Its a tie")
        done = True
        money += amount
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if done == True:
        tkinter.Button(gameWindow, text="5", command=betAmount5).place(x=455, y=400)  #create a button
        tkinter.Button(gameWindow, text="10", command=betAmount10).place(x=475, y=400)  #create a button
        tkinter.Button(gameWindow, text="25", command=betAmount25).place(x=500, y=400)  #create a button
        tkinter.Button(gameWindow, text="50", command=betAmount50).place(x=525, y=400)  #create a button
        tkinter.Button(gameWindow, text="OK", command=new_game).place(x=565, y=400)
        reset_button = tkinter.Button(gameWindow, text="New Game", command=new_game, bg='green')
        reset_button.place(x=275,y=400)
        player_button = tkinter.Button(gameWindow, text="     ", padx=8, bg='gray')
        player_button.place(x=220,y=350)
        player_button = tkinter.Button(gameWindow, text="     ", padx=8, bg='gray')
        player_button.place(x=350,y=350)

#Show the winner when the player hits
def hitting():
    global done
    global stay
    global bust
    global money
    global amount
    player_hand.append(getCard(player_card_frame))
    player_score = calcScore(player_hand)
    playerScore.set(player_score)

    player_button = tkinter.Button(gameWindow, text="               ", padx=8, bg='gray')
    player_button.place(x=275,y=400)
    player_button = tkinter.Button(gameWindow, text="Hit", command=hitting, padx=8, bg='cyan')
    player_button.place(x=220,y=350)
    dealer_button = tkinter.Button(gameWindow, text="Stay", command=staying, padx=5, bg='orange')
    dealer_button.place(x=350,y=350)


    if player_score > 21:
        winner.set("You busted...")
        bust = True
        done = True
        amount = 0
        tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
        tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
        tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)
    if done == True:
        tkinter.Button(gameWindow, text="5", command=betAmount5).place(x=455, y=400)  #create a button
        tkinter.Button(gameWindow, text="10", command=betAmount10).place(x=475, y=400)  #create a button
        tkinter.Button(gameWindow, text="25", command=betAmount25).place(x=500, y=400)  #create a button
        tkinter.Button(gameWindow, text="50", command=betAmount50).place(x=525, y=400)  #create a button
        tkinter.Button(gameWindow, text="OK", command=new_game).place(x=565, y=400)
        reset_button = tkinter.Button(gameWindow, text="New Game", command=new_game, bg='green')
        reset_button.place(x=275,y=400)
        player_button = tkinter.Button(gameWindow, text="     ", padx=8, bg='gray')
        player_button.place(x=220,y=350)
        player_button = tkinter.Button(gameWindow, text="     ", padx=8, bg='gray')
        player_button.place(x=350,y=350)


def initial_deal():
    hitting()
    dealer_hand.append(getCard(dealer_cardFrame))
    dealerScore.set(calcScore(dealer_hand))
    hitting()

def new_game():
    global dealer_cardFrame
    global player_card_frame
    global dealer_hand
    global player_hand
    global done
    global stay
    global bust

    done = False
    stay = False
    bust = False
    # embedded frame to hold the card images


    tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
    tkinter.Label(gameWindow, text="                        ").place(x=465, y=375)
    tkinter.Button(gameWindow, text="  ", bg="gray").place(x=455, y=400)  #create a button
    tkinter.Button(gameWindow, text="    ", bg="gray").place(x=475, y=400)  #create a button
    tkinter.Button(gameWindow, text="    ", bg="gray").place(x=500, y=400)  #create a button
    tkinter.Button(gameWindow, text="    ", bg="gray").place(x=525, y=400)  #create a button
    tkinter.Button(gameWindow, text="     ", bg="gray").place(x=565, y=400)

    shuffle()

    dealer_cardFrame.destroy()
    dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
    dealer_cardFrame.place(x=280,y=150)
    
    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(gameWindow, bg="black")
    player_card_frame.place(x=280,y=250)

    winner.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)

def betAmount5():
    global money
    global amount
    global done
    if money >= 5:
        amount += 5
        money -= 5
    tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
    tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)

def betAmount10():
    global money
    global amount
    global done
    if money >= 10:
        amount += 10
        money -= 10
    tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
    tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)

def betAmount25():
    global money
    global amount
    global done
    if money >= 25:
        amount = 25
        money -= 25
    tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
    tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)

def betAmount50():
    global money
    global amount
    global done
    if money >= 50:
        amount += 50
        money -= 50
    tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
    tkinter.Label(gameWindow, text="Pot: %d   " %(amount), bg="white").place(x=465, y=350)

gameWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
# this is a comment.
gameWindow.title("BlackJack")
gameWindow.geometry("640x480")

tkinter.Label(gameWindow, text='BlackJack', fg='black', font=('Consolas', 30,BOLD)).place(x=210, y=10)

tkinter.Label(gameWindow, text="Balance: %d   " %(money), bg="white").place(x=465, y=430)
tkinter.Label(gameWindow, text="Choose Bet:   ", bg="white").place(x=465, y=375)
tkinter.Label(gameWindow, text="Pot: %d   " %(amount*2), bg="white").place(x=465, y=350)

tkinter.Button(gameWindow, text="Exit", command=gameWindow.destroy, bg="red", fg="white").place(x=610, y=0)  #create a button


winner=tkinter.StringVar()
result = tkinter.Label(gameWindow, textvariable=winner,fg='black',font=('Consolas', 15, BOLD))
result.place(x=250,y=50)
 
dealerScore = tkinter.IntVar()
tkinter.Label(gameWindow, text="Dealer Total:", fg="black",bg="white").place(x=277,y=80)
tkinter.Label(gameWindow, textvariable=dealerScore, fg="black",bg="white").place(x=277,y=100)
# embedded frame to hold the card images
dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
dealer_cardFrame.place(x=100,y=80)

playerScore = tkinter.IntVar()


tkinter.Label(gameWindow, text="Your Total:", fg="black",bg="white").place(x=277,y=350)
tkinter.Label(gameWindow, textvariable=playerScore,fg="black",bg="white").place(x=277,y=370)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(gameWindow, bg="black")
player_card_frame.place(x=100,y=200)


shuffle_button = tkinter.Button(gameWindow, text="Shuffle", command=shuffle, padx=2, bg='yellow')
shuffle_button.place(x=590,y=40)

def msg():
   tkinter.messagebox.showinfo("Info", "Made by BVFreak.")
btn = tkinter.Button(gameWindow, text="Info", command=msg, bg="blue", fg="white")
btn.place(x=0,y=0)


# load cards
cards = []
getCardImages(cards)

deck = list(cards) + list(cards) + list(cards)
shuffle()

tkinter.Button(gameWindow, text="5", command=betAmount5).place(x=455, y=400)  #create a button
tkinter.Button(gameWindow, text="10", command=betAmount10).place(x=475, y=400)  #create a button
tkinter.Button(gameWindow, text="25", command=betAmount25).place(x=500, y=400)  #create a button
tkinter.Button(gameWindow, text="50", command=betAmount50).place(x=525, y=400)  #create a button
tkinter.Button(gameWindow, text="OK", command=new_game).place(x=565, y=400)

def ok():
    # Create the list to store the dealer's and player's hands
    dealer_button = tkinter.Button(gameWindow, text="Stay", command=staying, padx=5, bg='orange')
    dealer_button.place(x=350,y=350)
    dealer_hand = []
    player_hand = []
    initial_deal()
    new_game()

# loop
gameWindow.mainloop()