#Importing random
import random
#Initializing Global Variables
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
suits = ['Spades','Hearts','Diamonds','Clubs']
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
#Creating a dictionary with ranks and values
rv = {(key, value) for (key, value) in zip(ranks,values)}

#Creating the Classes
class Card:
    def __init__(self,rv,suit):
        self.rank = rv[0] #from Ace till King
        self.value = rv[1] #from 1 till 11
        self.suit = suit #Spades, Hearts, Diamonds, Clubs
        self.name = rv[0] + ' of ' + suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card in rv:
                #creating each card and appending it to the deck
                self.deck.append(Card(card,suit))
        random.shuffle(self.deck)#Shuffling the deck

    def deal(self,player,dealer):
        for _ in range(2):
            player.hand.append(self.deck.pop())
            dealer.hand.append(self.deck.pop())
    def dcard(self):
        return self.deck.pop()

class Player:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.stands = bool(0)
        self.busts = bool(0)
        self.hand = []

    def bet(self):#Ask player to bet and check for balance
        while True:
            try:
                bet = int(input('Please set your betting amount: '))
                if bet > self.balance:
                    print(f'You cannot bet more than your current balance: {self.balance}')
                    continue
            except TypeError:
                print('Please enter an intiger for the betting amount')
                continue
            else:
                print(f'You bet: {bet}')
                self.balance -= bet
                return bet

    def hit(self,deck):# add a card to a hand
        self.hand.append(deck.dcard())

    def value(self):#check value of hand and set ace value
        value = 0
        acecount = 0
        for card in self.hand:
            if card.rank == 'Ace':
                acecount += 1
            value += card.value
            if value > 21 and acecount > 0:
                value -= 10
                acecount -=1
        return value

    def bust(self):#bust state
        self.busts = True

    def stand(self):#Stand state
        self.stands = True

    def win(self,amount):
        self.balance += amount*2
        print(f'You Won! your new balance is: {self.balance}')

    def lose(self):
        if self.busts:
            print('Your total is over 21')
            print(f'You lost! your new balance is: {self.balance}')
        else:
            print(f'You lost! your new balance is: {self.balance}')

    def draw(self,amount,player):
        player.balance += amount
        print(player.name +' and Dealer tie!!')

    def reset(self):#reset the status and hand of player
        self.busts = False
        self.stands = False
        self.hand = []

#Creating functions
def hitstand(player,deck):#Function to check if player wants to hit/stand
    x = input('Do you want to hit or stand? (press h or s): ')
    if x == 'h':
        player.hit(deck)
    else:
        player.stand()

def show(player,dealer):#function to print the player's and dealer's hand
    print("Dealer's Hand:")
    if player.stands:
        for i in range(0,len(dealer.hand),1):
            print('-'+ dealer.hand[i].name)
    else:
        print('<Hidden Card>')
        print('-'+ dealer.hand[1].name)
    print(player.name +"'s Hand:")
    for i in range(0,len(player.hand),1):
        print('-'+ player.hand[i].name)

def replay(player):#function to check if player wants to play again
    if player.balance > 0:
        try:
            x = input('Do you want to continue playing? (y/n): ')
            if x.lower() == 'y':
                play = True
                return play
            else:
                play = False
                return play
        except TypeError:
            print('You entered a number, Game is closing!')
            play = False
            return play
    else:
        try:
            x = input('Do you want to play again? (y/n): ')
            if x.lower() == 'y':
                blackjack()
            else:
                play = False
                return play
        except TypeError:
            print('You entered a number, Game is closing!')
            play = False
            return play

def blackjack():#Main game function
    print('Welcome to BlackJack!\n'\
    'The rules are simple:\n'\
    "Your hand's value must be higher than the Dealer's without going over 21\n"\
    "The Ace's value can be 1 or 11\n"\
    'After you stand, the dealer will hit until he wins or busts\n'\
    'Good Luck and Have Fun !!')
    #requesting player name
    p1 = input('Please enter your player name: ')
    while True:
        try:
            p2 = int(input('Please deposite your chips: '))
        except:
            print('Please enter an intiger for the number of chips')
            continue
        else:
            print(f'Your Balance is: {p2}')
            break
    #initiaing player and dealer
    dealer = Player('Dealer',9000)
    player = Player(p1,p2)
    play = True#initializing main loop indicator
    #Main game loop
    while play:
        bet = player.bet()#ask player to bet
        deck = Deck()#create a deck and shuffle it
        #clear hands & player status
        dealer.reset()
        player.reset()
        #deal cards
        deck.deal(player,dealer)
        #printing hands
        show(player,dealer)
        #loop asking for hit/stand, printing hand and checking for bust
        while (not player.stands) and (not player.busts):
            hitstand(player,deck)
            if player.stands == True:
                print(player.name +" Stands, Dealer's Turn!!")
                show(player,dealer)
                break
            show(player,dealer)
            if player.value() > 21:
                player.bust()
                player.lose()
        if player.busts or (not play):
            pass
        else:
            while True:
                if dealer.value() > 21:
                    player.win(bet)
                    break
                elif dealer.value() > player.value():
                    player.lose()
                    break
                elif dealer.value() == player.value():
                    player.draw(bet,player)
                else:
                    dealer.hit(deck)
                    show(player,dealer)
                    continue
        play = replay(player)

blackjack()
