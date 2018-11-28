# building a casino game
# empty list [] to as your wallet to add your winnings to
#they need to stop playing and cashout
# let the player set the dollar/cents amount of the bet (in the game).
# let them continue playing as long as they have money or decide to cash out.
# Bonus, Do not allow bets for more then is in the wallet.
# Bonus 2, Display the odds of wining that round of the game (very advanced and may not work with every game)

# roulette, range of 38, which is 360 degrees plus a 0 and 00 + 1-36, 13 red, 13 black, the zeros are green
#evens are red, odds are black
# #welcome to the casino  the house is giving you 100 bucks in your wallet [] to start  also dont forget you can use the modulus assignment for the evens and odds



# #welcome to the casino  the house is giving you 100 bucks in your wallet [] to start  also dont forget you can use the modulus assignment for the evens and odds

# green 0 winning == bet + (bet * 100)

# #welcome to the casino  the house is giving you 100 bucks in your wallet [] to start  also dont forget you can use the modulus assignment for the evens and odds

from random import randint



def welcome():
  print('Welcome to the Devsino!\n' + 'would you like to play some roulette?')
  answer = input().lower()
  if answer == 'yes':
    print('well then go ahead and roll the ball!')
    wheel()
  elif answer == 'no':
    print('sorry to hear that, come again soon!')
  else:
    print('i didnt catch that...try again.')  
    welcome()
 
def wheel():
  print('hit return to roll')
  roll = input()
  if roll == "":
    roll = randint(0, 37)
  if roll % 2 == 0:
    print(f"Red {roll}")# bug, when rolled, 0 returns as a red cus there is no remainder
    wheel()
  if roll % 2 == 1:
    print(f"Black {roll}") 
    wheel()
  if roll == 0: #use isinstance to make this work?
    print(f"Green {roll}")  
    wheel()
  

   
# green = [0]
# red = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
# black = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

# # betting system
# def wager():
#   bet = input().lower()
#   if bet == red or black or green:
#     return bet + wallet.append()
#     print('Winner Winer!')
#  #betting by color

 #betting by number

 #betting by even or odd
# color winnings == bet + (bet * 2)
# number winnings == bet + (bet * 10)
# even/odd winnings == bet + (bet * 2)
# green 0 winning == bet + (bet * 100)

 
    
  
welcome() 



