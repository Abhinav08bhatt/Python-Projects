from time import sleep
from random import randint
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_key():
    style("\nPress ENTER to ROLL THE DIE...")
    input()

def style(s,n=0.03):
    '''
    nothing, just attention to details
    :param s: string input
    :param n: speed of text (default 0.04)
    '''
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

def int_input(s):
    style(s)
    try :
        x = int(input("\n> "))
        return x
    except :
        style("\nWrong input\n\n")
        return int_input(s)
    
def game_outline():
    '''
    return :
    number of player
    the final winning score
    '''
    num = int_input("Enter the number of players : (1-5) - ")
    end = int_input("Enter the winning score - ")
    return num,end

def roll_die():
    '''
    1 and 6 are included
    '''
    return randint(1,6)

def outcome_1():
    style("\n\nUh-oh... the die landed on 1.\n")
    style(f"You ran out of Luck. This round ends with  points.\n")


def outcome_others(points):
    style("\n\nLucky roll!\n")
    style(f"You earned {points} points from this outcome.\n")

def player_input(player_num,score,end_score):
    print("\n==================================================")
    style(f"                    PLAYER {player_num}\n")
    print("==================================================")
    bet = int_input("Enter the number of times u want to roll the die - ")
    chance_score = 0
    for chance in range (1,bet+1):
        press_key()
        outcome = roll_die()
        style(f"The outcome was : {outcome}")
        if outcome == 1 :
            outcome_1()
            chance_score = 0
            break    
        else :
            outcome_others(outcome)
            chance_score += outcome
    print("\n")
    style(f"You earned {chance_score} points in this round!!!\n")
    score += chance_score
    if score >= end_score:
        return score
    style(f"Final score is now : {score}\n")
    sleep(2)
    return score

def ui(player_score,end_score):
    
    print("==================================================")
    print(f"Score to reach : {end_score}")
    print("==================================================")
    for i in range (0,len(player_score)):
        print(f"{player_score[i][0]} : {player_score[i][1]}")
    print("==================================================")


def game():
    
    number_of_players,end_score = game_outline()
    players_score=[
    ]
    for i in range (1,number_of_players+1):
        players_score.append([f"Player {i}",0])

    while True:
        for player in range (0,number_of_players):
            clear()
            ui(players_score,end_score)
            players_score[player][1] = player_input(player+1,players_score[player][1],end_score)
            if players_score[player][1] >= end_score:
                clear()
                ui(players_score,end_score)
                style(f"Congratulations {player+1} WON!!!\n")
                return
            clear()
        

if __name__ == "__main__":
    clear()
    game()