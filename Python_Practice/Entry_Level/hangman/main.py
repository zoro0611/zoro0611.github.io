import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lifeCount = 6
#randomly get a word from the word_list
chosenWord = random.choice(word_list)
print(f'The answer is {chosenWord}.')
display = []
guessList = []
for n in range(len(chosenWord)):
    display.append('_')
print(display)
gameIsOver = False
#當display裡還有'_'時，繼續遊戲
while '_' in display and not gameIsOver:
    #猜一個字母
    userInput = input('Guess a letter:\n').lower()
    #如果猜過了，就放進guessList
    if userInput in guessList:
        print(f'You have already guessed {userInput}.')
    #如果沒猜過，就繼續
    else:
        #放進guessList
        guessList.append(userInput)
        #如果猜對，就把display裡的'_'換成猜的字母
        if userInput in chosenWord:
            print(f'你輸入{userInput}猜對了')
            for ind in range(len(chosenWord)):
                if userInput == chosenWord[ind]:
                    display[ind] = userInput
        #如果猜錯，就lifeCount - 1
        else:
            print(f'你猜{userInput}錯了')
            lifeCount -= 1
        print(display)
        print(stages[lifeCount])
        #如果lifeCount = 0，就輸了
        if lifeCount == 0:
            print('You lose.')
            gameIsOver = True
            break
        elif '_' not in display:
            print('You win. GameOver')
            gameIsOver = True
            break
