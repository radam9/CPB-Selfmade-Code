#Milestone project 1 TIC TAC TOE
#Importing Modules
import random
#Function to print the board
def board(num):
    print('     #     #     \n'\
          f'  {num[7]}  #  {num[8]}  #  {num[9]}  \n'\
          '     #     #     \n'\
          '#################\n'\
          '     #     #     \n'\
          f'  {num[4]}  #  {num[5]}  #  {num[6]}  \n'\
          '     #     #     \n'\
          '#################\n'\
          '     #     #     \n'\
          f'  {num[1]}  #  {num[2]}  #  {num[3]}  \n'\
          '     #     #     \n')
#Requesting input from player and assigning the location value
def turn(b,num,player,p):
    while True:
        x = int(input(f"It's {p[player]}'s turn!, Enter a location: "))
        if x < 1 or x > 9:
            print('Please enter a value between 1 and 9')
        else:
          if x in b:
              print('That spot is already taken! Choose another one.')
              continue
          else:
              if player == 1:
                  num[x] = 'X'
              else:
                  num[x] = 'O'
              return b.append(x), num[x]
#Request to play again
def replay():
    x = input('Do you want to play again? (y/n)\n')
    if x.lower()=='y':
        tictactoe()
    else:
        end = 1
        return end
#Check if someone won
def check(num,p,player,b):
    #Variable with possible solutions
    end = 0
    solution = [ num[1]+num[2]+num[3] , num[4]+num[5]+num[6] , num[7]+num[8]+num[9] , \
    num[1]+num[4]+num[7] , num[2]+num[5]+num[8], num[3]+num[6]+num[9] , \
    num[1]+num[5]+num[9] , num[3]+num[5]+num[7] ]
    if 'OOO' in solution or 'XXX' in solution:#Check if someone won
        print(f'Congratulations, Player {p[player]} has won!')
        end = 1
    elif len(b) == 9:#check for a draw
        print('The Game is a Draw!!')
        end = 1
    return end
#Main game function
def tictactoe():
    #Printing the Welcome message and Rules
    print('Welcome to TIC TAC TOE!\n'\
            'The rules are simple.\n''# X will start first\n'\
            '# The board is represted as the number pad 1->9\n'\
            '# Choosing a number will print the X or O in the corresponding location on the board\n'\
            'Have fun')
    #Requesting the players' names
    p = ['Player 1','Player 2']
    p[0] = input("Enter the First player's name: ")
    p[1] = input("Enter the Second player's name: ")
    #Requesting the start order
    start = int(input(f'Who will play first?\nChoose 1 for {p[0]}\nChoose 2 for {p[1]}\nChoose 3 for Random : '))
    if start == 1:#Player 1 starts
        player = bool()
    elif start == 2:#Player 2 Starts
        player = bool(1)
    else:#Choosing starting player Randomly
        player = bool(random.randint(0,1))
    b = [] #initiating empty board, also used as a numer of turns counter
    num = [' ']*10 #Initiating the empty board slots
    end = 0 #Program Close
    while end==0:
        turn(b,num,player,p)
        board(num)
        end = check(num,p,player,b)
        if end == 1:
            end = replay()
        player = not player

tictactoe()
