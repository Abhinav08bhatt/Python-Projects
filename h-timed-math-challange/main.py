from random import randint,choice
from time import time
import os

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUS = 10


def clear():
    '''
    to clear the terminal for a better console UI
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def correct_input():
    try:
        ans = int(input("> "))
        return ans
    except:
        return 0
    
def generate_question():
    left = randint(MIN_OPERAND,MAX_OPERAND)
    operator = choice(OPERATORS)
    right = randint(MIN_OPERAND,MAX_OPERAND)

    expression = f"{str(left)} {operator} {str(right)}"
    answer = eval(expression)
    
    return expression,answer

def main():
    number_of_attempts = 0
    start = time()
    for i in range(TOTAL_QUS):
        exp,ans = generate_question()
        while True:
            print(f"problem {i+1} # {exp}")
            guess = correct_input()
            number_of_attempts += 1
            if guess == ans:
                clear()
                print("CORRECT!!!\nNEXT QUESTION...\n")
                break
            clear()
            print("WRONG!!!\nTRY AGAIN...\n")
    end = time()
    time_taken = round((end-start),2)
    print(f'''
U did 10 questions and it took u {number_of_attempts} attempts and {time_taken} seconds
''')
    
clear()
main()