from random import randint
from time import sleep
import os

def clear():
    '''
    to clear the terminal for a better console UI
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def style(s,n=0.04):
    '''
    nothing, just attention to details
    :param s: string input
    :param n: speed of text (default 0.04)
    '''
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

def press_key():
    input("\n\nPress ENTER to continue...")

def valid_in():
    '''
    takes the different inputs but find the closest and return : r for rock , p for paper and s for scissors 
    possibilities : r R rock ROCK Rock rk rock (so we will focus on starting word...if its and ask the user if the user if they mean it)
    '''
    while True:
        user = input("\n\nEnter your side : ").lower()
        if not user:
            style("\nEmpty input...\nTry Again...",0.02)
            sleep(1)
            continue

        if user[0]=='r':
            if user == 'r' or user =='rock':
                user = 'r'
                return user
            else:
                ask = input("Did you mean ROCK ? (y/n) : ")
                if ask == 'y':
                    user = 'r'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        elif user[0]=='p':
            if user == 'p' or user =='paper':
                user = 'p'
                return user
            else:
                ask = input("Did you mean PAPER ? (y/n) : ")
                if ask == 'y':
                    user = 'p'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        elif user[0]=='s':
            if user == 's' or user =='scissors':
                user = 's'
                return user
            else:
                ask = input("Did you mean SCISSORS ? (y/n) : ")
                if ask == 'y':
                    user = 's'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        else:
            style("\nummm, we could not guess your input.\nTry Again...",0.02)
            sleep(2)

def computer_turn():
    '''
    Using the random randint to get the random move from a list of rock paper scissors
    '''
    moves = ['r','p','s']
    return moves[randint(0,2)]

def game_logic(player1,player2):
    '''
    creating the function to check who wins, as rock beats scissors, scissors beats paper and paper beats rock
        
    :param player1: r - p - c
    :param player2: r - p - c

    :return 1(player 1 wins) - 2(player 2 wins) - 0{tie} - 3(some logical issue)
    '''
    if player1 == player2 :
        return 0
    elif player1=='r' and player2=='p':
        return 2
    elif player1=='p' and player2=='s':
        return 2
    elif player1=='s' and player2=='r':
        return 2
    elif player1=='r' and player2=='s':
        return 1
    elif player1=='s' and player2=='p':
        return 1
    elif player1=='p' and player2=='r':
        return 1
    else:
        return 3
    
def ui(user_points,computer_points,points_to_win):

    while user_points<points_to_win and computer_points<points_to_win:
        print(f"User : {user_points:>3} | Computer : {computer_points:>5}")

        style(f"\nROCK{'.'*3}",0.02)
        sleep(0.5)
        style(f"PAPER{'.'*3}",0.02)
        sleep(0.5)
        style(f"SCISSORS{'.'*3}",0.02)
        sleep(0.5)
        
        user = valid_in()
        computer = computer_turn()

        result = game_logic(user,computer)

        if result == 0:
            print(f"\nUser : {user:>3} | Computer : {computer:>3}\n")
            style("The game was a tie...\nAgain...")
        elif result == 1:
            user_points += 1
            print(f"\nUser : {user:>3} | Computer : {computer:>3}\n")
            if user_points == points_to_win:
                return 1
            style(f"User Won!!!\n{points_to_win-user_points} more to win!")
        elif result == 2:
            computer_points += 1
            print(f"\nUser : {user:>3} | Computer : {computer:>3}\n")
            if computer_points == points_to_win:
                return 0
            style(f"Computer Won!!!\n{points_to_win-computer_points} more to win!")
        elif result == 3:
            print(f"\nUser : {user:>3} | Computer : {computer:>3}\n")
            print("We are facing some logical issue")
            
        press_key()
        clear()


def game():

    style("Welcome...\nReady for a ROCK...PAPER...SCISSORS game?\n")
    points_to_win = int(input("Match of how many points ? \n(enter positive int) : "))
    style(f"\nAlright, first to score {points_to_win} points wins!\n")
    sleep(0.4)
    style("!!!ALL THE BEST!!!\n\n",0.06)
    sleep(1)
    clear()

    user_points = 0
    computer_points = 0

    result = ui(user_points,computer_points,points_to_win)
    if result == 1:
        style("\nCONGRATULATIONS!!!\n",0.03)
        sleep(0.3)
        style("You outsmarted the computer and WON!\n",0.03)
        sleep(0.3)
        style("Rock. Paper. Scissors. DESTINY.\n",0.04)
    else:
        style("\nBetter luck next time...\n",0.03)
        sleep(0.3)
        style("The computer takes the win this round\n",0.03)
        sleep(0.3)
        style("But hey… you can always challenge it again!\n",0.04)

if __name__ == "__main__":

    clear()

    game()
