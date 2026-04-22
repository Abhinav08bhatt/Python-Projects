# QUIZ GAME

'''TO CLEAR THE TERMINAL FOR CLEAN LOOK (works on windows, linux and mac)'''
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
'''----------------------------------------------------------------------'''

'''TO MAKE THE PROGRAM SLOW WHEN NEEDED'''
from time import sleep
def press_key():
    input("\n\nPress ENTER to continue...")
'''------------------------------------'''

def qus_ans():
    lst = [
        [
            "What does CPU stand for?",
            "central processing unit"
        ],
        [
            "What does GPU stand for?",
            "graphics processing unit"
        ],
        [
            "What does RAM stand for?",
            "random access memory"
        ],
        [
            "What does HTML stand for?",
            "hypertext markup language"
        ],
        [
            "What does AI stand for?",
            "artificial intelligence"
        ]
    ]
    return lst # question are from 1 not from 0


def ui(score,number,qus,ans,correct):
    answer = input(f"SCORE : {score}\nQUESTION {number} : {qus}\nENTER ANS :  ")
    
    if answer.strip().lower() == ans:
        score += 5
        correct += 1
        print(f"\n\nAmazing! Correct answer!!!\n5 points has been added to your total score\nSCORE : {score}")
        press_key()
        clear()
        return score,correct
    else:
        score -= 1
        print(f"\n\nWRONG ANSWER\nCorrect answer was : {ans}\nYour answer : {answer}\n1 point has been deducted from your total score\nSCORE : {score}")
        press_key()
        clear()
        return score,correct

def game():
    score = 0
    correct_questions = 0
    book_list = qus_ans()

    for i in range (0,len(book_list)):
        score,correct_questions = ui(score,i+1,book_list[i][0],book_list[i][1],correct_questions)
    
    exit_game(score,correct_questions,len(book_list))    


def exit_game(score=None,correct=None,length=None):
    if score == None and correct == None and length == None : # the game was never played
        print("Thank you for showing your interest,\nSee you next time. Bye")
    else:
        # show the score and ending message.
        print(f"Amazing attempt\nYou did {correct} questions correct and {length-correct} wrong\nTOTAL SCORE : {score}")
        print("Thank you for showing your interest,\nSee you next time. Bye")


if __name__ == "__main__":

    # clearing the terminal 
    clear()

    # welcome message : 
    print("Welcome to my COMPUTER QUIZ !!!")

    # asking for the wish to play : 
    ask = input("Do you wish to play the game ? \nENTER (yes/no): ")
    if ask.lower() != 'yes':
        clear()
        exit_game()
    else:
        clear()
        game()