#J,Q,K = 10
#A = 1 or 11
#if <=16, must take one more card

import random

def init_cards():
    num = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cardsDict = {
        "Spade": num.copy(),
        "Heart": num.copy(),
        "Diamond": num.copy(),
        "Club": num.copy(),
    }
    return cardsDict

deckCards = init_cards()

computer_cards = []
player_cards = []

#check if player or computer's total below 17, if yes then deal one more card
def check_total(empty_list):
    if sum(empty_list) <= 16:
        deal_cards(empty_list)
        check_total(empty_list)
    elif sum(empty_list) > 21:
        ifAdjustAce(empty_list)
        check_total(empty_list)
def computer_turn(recursion_depth=0):
    if recursion_depth > 10:
        return
    if sum(computer_cards) < 21:
        if sum(computer_cards) > player_cards[0]:
            wantMore = random.choice(["y","n"])
            if wantMore == "y":
                deal_cards(computer_cards)
                computer_turn(recursion_depth=recursion_depth+1)
            else:
                return
        elif sum(computer_cards) <= player_cards[0]:
            deal_cards(computer_cards)
            computer_turn(recursion_depth=recursion_depth+1)
    elif sum(computer_cards) == 21:
        return
    elif sum(computer_cards) > 21:
        ifAdjustAce(computer_cards)
        check_total(computer_cards)
        computer_turn(recursion_depth=recursion_depth+1)
def runGame(computer_cards, player_cards):
    computer_turn()
    ifAdjustAce(computer_cards)
    ifAdjustAce(player_cards)
    print("Computer's cards: ")
    print(computer_cards)
def deal_cards(empty_list):
    suit = random.choice(list(deckCards.keys()))
    if len(deckCards[suit]) == 0:
        del deckCards[suit]
        suit = random.choice(list(deckCards.keys()))
    number = random.choice(deckCards[suit])
    deckCards[suit].remove(number)
    empty_list.append(number)
def ifAdjustAce(cards):
    if sum(cards) > 21:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
                if sum(cards) <= 21:
                    break
def checkWinner(computer_cards, player_cards):
    sumCom = sum(computer_cards)
    sumPyr = sum(player_cards)
    if sumPyr == 21:
        print('You win!')
    else:
        if sumCom == 21:
            print('You lose!')
        elif sumCom > 21:
            if sumPyr > 21:
                print('Draw!')
            else:
                print('You win!')
        elif sumCom < 21:
            if sumPyr > 21:
                print('You lose!')
            elif sumCom > sumPyr:
                print('You lose!')
            elif sumCom < sumPyr:
                print('You win!')
            elif sumCom == sumPyr:
                print('Draw!')

for i in range(2):
    deal_cards(player_cards)
    deal_cards(computer_cards)
check_total(player_cards)
check_total(computer_cards)

print(f"Computer's first card: {computer_cards[0]}")
print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
playerContinue = True
while playerContinue:
    if sum(player_cards) == 21:
        playerContinue = False
    else:
        if sum(player_cards) > 21:
            playerContinue = False
        else:
            askInput=input('Do you want to get one more card? Type "y" for yes, "n" for no. Your answer: ')
            if askInput == 'y':
                deal_cards(player_cards)
                print('Your cards:  ')
                print(player_cards)
                ifAdjustAce(player_cards)
                if sum(player_cards) > 21:
                    runGame(computer_cards, player_cards)
                    playerContinue = False
            else:
                playerContinue = False


runGame(computer_cards, player_cards)
sumCom = sum(computer_cards)
sumPyr = sum(player_cards)
print(f'Computer has {sumCom} points')
print(f'You have {sumPyr} points')
checkWinner(computer_cards, player_cards)
