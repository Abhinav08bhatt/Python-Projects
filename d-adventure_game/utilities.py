import os
from time import sleep

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
