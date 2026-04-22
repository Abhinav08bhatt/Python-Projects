# Number guessing game

'''TO CLEAR THE TERMINAL FOR CLEAN LOOK (works on windows, linux and mac)'''
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
'''----------------------------------------------------------------------'''

'''TO GENERATE RANDOM NUMBER'''
from random import randint # randint( lower-limit , upper-limit ) both the limits are included
def random_number(upper):
    return randint(0,upper)
'''-------------------------'''

'''TO MAKE THE PROGRAM SLOW WHEN NEEDED'''
from time import sleep
def press_key():
    input("\n\nPress ENTER to continue...")
'''------------------------------------'''

def int_input(option=0): # 0 for Guess input (default), 1 for Upper Input
    if option == 0:
        while True:
            guess = input("Guess the number : ")
            try : 
                guess = int(guess)
                if guess>=0:
                    return guess
                else :
                    print("Wrong input, enter a positive integer value...")
            except :
                print("Wrong input, enter a positive integer value...")
    elif option == 1:
        while True:
            upper = input("Enter the UPPER LIMIT : ")
            try : 
                upper = int(upper)
                if upper>=0:
                    return upper
                else :
                    print("Wrong input, enter a positive integer value...")
            except :
                print("Wrong input, enter a positive integer value...")


def ui(attempt,number):
    while True:
        print(f"Attempt number : {attempt}\n")
        guess = int_input()
        attempt += 1
        if guess>number:
            style("Try lower...",0.05)
            sleep(1)
            clear()
        elif guess<number:
            style("Try higher...",0.05)
            sleep(1)
            clear()
        else:
            return 1,attempt

def style(s,n=0.04): # input , speed(default = 0.04)
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

'''----------------------------File handling-----------------------------'''
import sqlite3 # need to learn this
conn = sqlite3.connect("b-number-guessing_game/scores.db")
conn.execute('CREATE TABLE IF NOT EXISTS scores (name TEXT, attempts INTEGER)')
conn.commit()

def add_score(name,attempts):
    conn.execute('INSERT INTO scores (name, attempts) VALUES (?,?)',(name,attempts))
    conn.commit()

    conn.execute('DELETE FROM scores WHERE rowid NOT IN (SELECT rowid FROM scores ORDER BY attempts ASC LIMIT 5)')

def get_score():
    return conn.execute('SELECT name, attempts FROM scores ORDER BY attempts ASC LIMIT 5').fetchall()

def clear_score():
    conn.execute('DELETE FROM scores')
    conn.commit()
    print("All scores have been cleared")

def top_5(db):
    clear()
    style(f"TOP 5 PLAYERS ARE : \n")
    style("  NAME     |     ATTEMPTS   \n")
    for i in range (0,len(db)):
        print(f"   {db[i][0]:15} {db[i][1]:<5}")
        sleep(0.05)
'''----------------------------File handling-----------------------------'''

def game():
    attempt = 0
    upper = int_input(1)
    number = random_number(upper)

    score_data = get_score()
    score_attempts_list = []
    for i in range (0,len(score_data)):
        score_attempts_list.append(score_data[i][1])

    string = f"\nThe number has been chosen...\nThe number is somewhere between 0 and {upper}\n\nTRY GUESSING THE NUMBER IN LEAST ATTEMPTS..."
    style(string,0.04)
    sleep(0.5)
    style("\n\n...ALL THE BEST...",0.06)
    sleep(1.5)
    clear()

    outcome,attempt = ui(attempt,number)

    if outcome == 1:
        clear()
        style("Congratulations!!!")
        sleep(0.2)
        style(f"\n{number} is the CORRECT GUESS! ")
        sleep(0.2)
        style(f"\nIt took you {attempt} tries to guess it!!!")
    
    if len(score_attempts_list)<5 or attempt<max(score_attempts_list):
        name = input("\n\nCongratulations!!!\nYour score was in top 5...\nEnter your name for the score board : ")
        add_score(name,attempt)
        clear()
        top_5(get_score())
        

if __name__ == "__main__":
   
    # clearing the terminal 
    clear()
    

    # the game ------------
    game()