
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print('Welcome to the auction program.')
bidDic = {}
auctionDone = False
while not auctionDone:
  
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))
  bidDic[name] = bid
  #clear console
  print('\n'*100)

  over = input('Are there any other bidder? Type "yes" or "no".\n')
  if over == 'no':
    auctionDone = True

topBid = 0
topBidder = ''
for bidder in bidDic:
  if bidDic[bidder] > topBid:
    topBid = bidDic[bidder]
    topBidder = bidder
print(f'The winner is {topBidder} with a bid of ${topBid}.') 
