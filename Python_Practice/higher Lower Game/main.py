# step1: import art and game_data
from art import logo, vs
from data import data 
import random

# step2: global variables
score = 0
totalDataLength = len(data)
gameData = []
game_over = False
used_data = []
a_object = {}
b_object = {}
# step3: functions
def ShowGameLogo():
    print(logo)
def ShowGameVs():
    print(vs)
def InitialGame():
    global gameData
    gameData = data.copy()
    a = random.choice(gameData)
    gameData.remove(a)
    used_data.append(a)
    global a_object
    a_object = a
def ProcessGame():
    global gameData
    b = random.choice(gameData)
    gameData.remove(b)
    used_data.append(b)
    global b_object
    b_object = b
def printObjInfo(obj):
    print(f"Name: {obj['name']}, Description: {obj['description']}, Country: {obj['country']}")
def findAnswer(a_object, b_object):
    if a_object['follower_count'] > b_object['follower_count']:
        return 'A'
    else:
        return 'B'
# step4: main program

def CreateGame():
    global score
    global game_over
    global used_data
    global a_object
    global b_object
    InitialGame()
    while not game_over:
        if score == totalDataLength:
            game_over = True
            print("You have completed all the questions, you win!")
            break
        ShowGameLogo()
        ProcessGame()
        print('A: ')
        printObjInfo(a_object)
        ShowGameVs()
        print('B: ')
        printObjInfo(b_object)
        answer = findAnswer(a_object, b_object)
        print('Which one has more followers? Type "A" or "B"')
        user_input = input("Your answer: ").upper()
        print(f"A's number of followers is {a_object['follower_count']}, B's number of followers is {b_object['follower_count']}.")
        if user_input == answer:
            score += 1
            print(f"You are right! Your current score: {score}")
            if answer == 'B':
                a_object = b_object
        else:
            game_over = True
            print(f"You are wrong! Final score: {score}")
            InitialGame()
            break

ctnGame = True
while ctnGame:
    CreateGame()
    rtnInput = input('input "Y" to restart the game.')
    if rtnInput == 'Y':
        game_over = False
    else:
        ctnGame = False
        print('Goodbye!')