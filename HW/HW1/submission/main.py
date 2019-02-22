##File Name:  main.py
#Purpose:     Program that simulates a simple trivia game for 
#             two players who will take turns in answering 
#             questions
#Author:      Austin Ramberg
#Date:        January 22, 2019

#import question
from question import Question

# Initialize question objects and append to questionList
def initializeQuestions():

    outList = []

    question1 = Question('A spell raises an undead corpse for 10 minutes or until the spell is dispelled by the user. This spell would belong to which school of magic?', 'Abjuration', 'Necromancy', 'Illusion', 'Enchantment', 2)
    outList.append(question1)

    question2 = Question('A spell transports a creature from a different plane for 10 minutes or until the spell is dispelled by the user. This spell would belong to which school of magic?', 'Conjuration', 'Illusion', 'Transmutation', 'Divination', 1)
    outList.append(question2)

    question3 = Question('A spell manifests a magical construct of a wolf that fights for the caster for 10 minutes or until the spell is dispelled by the user. This spell would belong to which school of magic?', 'Illusion', 'Conjuration', 'Divination', 'Evocation', 4)
    outList.append(question3)

    question4 = Question('A spell creates a magical barrier in a 30 ft line that protects those behind it from all physical and magical project damage for 1 minute or until the spell is dispelled by the user. This spell would belong to which school of magic?', 'Transmutation', 'Evocation', 'Illusion', 'Conjuration', 2)
    outList.append(question4)

    question5 = Question('A spell changes the physical appearance of the target to someone the caster has seen before for 10 minutes or until the spell is dispelled by the user. This spell would belong to which school of magic?', 'Enchantment', 'Conjuration', 'Transmutation', 'Illusion', 3)
    outList.append(question5)

    question6 = Question('A spell slows the aging process of the target. This spell would belong to which school of magic?', 'Transmutation', 'Enchantment', 'Anjuration', 'Necromancy', 4)
    outList.append(question6)

    question7 = Question('A spell allows the caster to read the thoughts of a target for up to 1 minute or until it is dispelled by the user. This spell would belong to which school of magic?', 'Divination', 'Evocation', 'Enchantment', 'Illusion', 1)
    outList.append(question7)

    question8 = Question('The targets of a spell have their minds and sense deceived into thinking they are looking at a ferocious bear. This spell would belong to which school of magic?', 'Enchantment', 'Illusion', 'Divination', 'Conjuration', 2)
    outList.append(question8)

    question9 = Question('A spell negates the activation of a spell cast by another creature at a level equal to or less than the level this spell is cast at. This spell would belong to which school of magic?', 'Enchantment', 'Evocation', 'Abjuration', 'Necromancy', 3)
    outList.append(question9)

    question10 = Question('A spell transports its caster to another dimension. This spell would belong to which school of magic?', 'Enchantment', 'Conjuration', 'Evocation', 'Illusion', 2)
    outList.append(question10)

    return outList

def main():
    # global variables
    questionList = initializeQuestions()
    greeting = 'Welcome to the Spell Trivia Quiz!'
    roundCount = 1
    player1Score = 0
    player2Score = 0
    
    # Print user greeting
    print(greeting)
    print('_' * len(greeting) + '\n')

    # Game loop
    while roundCount <= len(questionList):
        currentQuestion = questionList[roundCount-1]
        if roundCount % 2 == 0:
            player = 'Player 2'
        else:
            player = 'Player 1'
        print(player + ' here is your question:')
        print(currentQuestion)
        while True:
            try:
                userAnswer = float(input("Enter your answer: "))
                if userAnswer not in [1,2,3,4]:
                    print('Your input was a number, but not between 1 and 4. Please try again.')
                    continue
                break
            except:
                print('Error: your answer has to be a value between 1 and 4. Try again.')
        if userAnswer == currentQuestion.getCorrectAnswer():
            print('Excellent! You score!\n')
            if player == 'Player 1':
                player1Score += 1
            else:
                player2Score += 1
        else:
            print('That is incorrect. Better luck with the next question.\n')
        roundCount += 1

    # Print final scores and winner
    print('And the final scores are:')
    print('Player 1: ' + str(player1Score))
    print('Player 2: ' + str(player2Score))
    if player1Score > player2Score:
        print('Player 1 wins!')
    elif player2Score > player1Score:
        print('Player 2 wins!')
    else:
        print('It\'s a tie!')

if __name__ == "__main__" :
    main()