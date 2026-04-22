'''
plan:

get the text of the file in a variable...
count the number of adjective,verb,place,name
loop the variable and ask for input : adjective 1 : give the input to function `replace word` replace that adjective with the input and return
and another input : adjective 2 : give the input and bla bla bla

problem?
idk the adjective verb name place or how many other type of placeholders will be there
but one thing is common : []
just if i can count how many [ are there and add the word net to them in a list...
like [ADJECTIVE]
look for [ word next to it is ADJECTIVE add it in the placeholder list = [adjective,verb,noun,etc]
then i can loop into the placeholder list and replace all  of then using the upper idea....
'''

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_word(word):
    '''
    :param word     : impure word
    function        : removes [ ] . , and give us a usable string
    return          : clean word
    '''
    word_list = list(word)
    while '[' in word_list:
        word_list.remove('[')
    while ']' in word_list:
        word_list.remove(']')
    while '.' in word_list:
        word_list.remove('.')
    while ',' in word_list:
        word_list.remove(',')
    while '?' in word_list:
        word_list.remove('?')
    while '!' in word_list:
        word_list.remove('!')
    word = "".join(word_list)
    return word

def search_words(text):
    '''
    :param text     : text of whole file 
    function        : to find the placeholder and the count of each placeholder
    return          : list of tuple containing placeholders with their count
    '''
    placeholder_words = []
    text_list = text.split()
    for word in text_list:
        if '[' in word:
            placeholder_words.append(clean_word(word))
    placeholder = []
    for i in placeholder_words:
        count = placeholder_words.count(i)
        placeholder.append((i,count))
    return list(dict.fromkeys(placeholder)) # removes duplicate values 

def read_file(file="g-madlibs-generator/story.txt"):
    '''
    :param file     : default
    function        : read the file and sent it to refinement
    return          : text of the file
    '''
    with open(file,"r") as f:
        text = f.read()
    return text
    # return search_words(text)
            
def replace_in_file(text,placeholder,word,file="g-madlibs-generator/story.txt"):

    with open(file,'w') as f:
        f.write(text.replace(f"[{placeholder}]",word,1))
    
def replace_placeholder(placeholder):
    for i in range (0,len(placeholder)):
        for j in range (0,placeholder[i][1]):
            text = read_file()
            word = input(f"Enter {placeholder[i][0]} {j+1} : ")
            replace_in_file(text,placeholder[i][0],word)

def main():

    clear()
    text = read_file()
    print('''==================== TEMPLATE TEXT ====================''')
    print(text)
    print('''=======================================================''')
    replace_placeholder(search_words(text))
    print('''====================== FINAL TEXT =====================''')
    print(read_file())
    print('''=======================================================''')

'''
DEFAULT STORY.TXT :

Yesterday, I traveled to the mysterious [PLACE].  
There, I met a [ADJECTIVE] [NOUN] guarding a glowing portal.  
The creature asked me to [VERB] before allowing me to pass.  
Surprisingly, the portal led to another [PLACE].  
A group of [PLURAL_NOUN] welcomed me with a very [ADJECTIVE] ceremony.  
We decided to spend the day learning how to [VERB].  
By sunset, I felt like a true [NOUN].  
It was, without a doubt, the most unforgettable [ADJECTIVE] adventure of my life!
'''


main()