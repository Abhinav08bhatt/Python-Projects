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

def int_input(s):
    style(s,0.01)
    try :
        x = int(input("\n> "))
        return x
    except :
        style("\nWrong input\n\n")
        return int_input(s)

def press_key():
    input("\n\nPress ENTER to continue...")

MONEY = 0

def rules():
    style(f'''
Rules : 
          
- You give the initial money
- The slot spins
    - If all 3 sides of slot are same, 
          - your balance money is multiplied by the number of slot
    - If sides are not same,
          - your balance money is divided by the max number in the slot
- You can quit at any given moment, or play until you run out of money!!!
''',0.01)

def deposit_money():
    amt = int_input("Enter the initial amount : ")
    return amt

def bet(amt):
    slot = []
    for i in range(0,3):
        slot.append(randint(1,3))
    if slot[0] == slot[1] == slot[2]:
        print(f"\nSLOTS : | {slot[0]} | {slot[1]} | {slot[2]} |")
        amt = amt*slot[0]
        style(f"\nLucky bet!!!\nYou {slot[0]}x your money, \nNow your balance is {amt}")
        press_key()
    else:
        print(f"\nSLOTS : | {slot[0]} | {slot[1]} | {slot[2]} |")
        amt = amt//max(slot)
        style(f"\nOOPS!!!\nYou got your money divided by {max(slot)}, \nNow your balance is {amt}")
        press_key()
    return amt

def main():

    balance_amt = deposit_money()

    r = input("Do you want to read rules ? [y/n] : ").lower()    
    if r == "y":
        rules()
    
    while balance_amt>=99:

        clear()

        command = input(f'''
BALANCE                    : {balance_amt}
======================================
Do you want to bet with your {balance_amt}?
You can get upto:
    3x : {balance_amt} x 3 = {balance_amt*3}
    2x : {balance_amt} x 2 = {balance_amt*2}
    1x : {balance_amt} x 1 = {balance_amt*1}
but also:
    3/ : {balance_amt} / 3 = {balance_amt//3}
    2/ : {balance_amt} / 2 = {balance_amt//2}
    1/ : {balance_amt} / 1 = {balance_amt//1}
OR you can play safe and quit with {balance_amt}, 

Your call, enter "b" to bet and "q" to quit :
> ''')    
        if command == "q" or command[0] == "q" :
            print(f"You made the decision...\nYou are going with {balance_amt}")
            return
        balance_amt = bet(balance_amt)
    if balance_amt <= 99:
        clear()
        style(f"\nYou don't have enough money to bet...\nCurrent balance : {balance_amt}\n")
        return

clear()
main()