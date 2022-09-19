import random_word


def print_greetings():
    print("******************************")
    print("Hello and welcome to the game!")
    print("******************************")

def print_list(a_list):
    print(a_list)

def get_word():
    r = random_word.RandomWords()
    word = r.get_random_word()
    return word

def string_to_list(a_word):
    position = 0
    length = len(a_word)
    a_list = []
    while position < length:
        a_list.append(a_word[position])
        position = position+1
    return a_list

def get_guess():
    print("Please give me a character")
    a_char = input()
    return a_char

def get_position_of_guess(a_char,a_list):
    position = 0
    pos_list = []
    while(position < len(a_list)):
        if a_list[position] == a_char:
            pos_list.append(position)
        position = position + 1
    return pos_list

def add_correct_letter(a_hidden_list,a_positions_list,a_char):
    position = 0
    while (position < len(a_positions_list)):
        a_hidden_list[a_positions_list[position]] = a_char
        position = position + 1    
    return hidden_list

def are_we_done(a_word_list,a_hidden_list):
    if a_word_list == a_hidden_list:
        return True
    else:
        return False
def print_hangman(number_of_incorrect_guesses):
    if number_of_incorrect_guesses == 1:
        print("""



        |        
        """)
    elif number_of_incorrect_guesses == 2:
        print("""


        |
        |     
        """)
    elif number_of_incorrect_guesses == 3:
        print("""

        |
        |
        |     
        """)        
    elif number_of_incorrect_guesses == 4:
        print("""
        |
        |
        |
        |   
        """)
    elif number_of_incorrect_guesses == 5:
        print("""
        |
        |
        |
        |   
        """)
    elif number_of_incorrect_guesses == 6:
        print("""
        ___
        |
        |
        |
        |   
        """)  
    elif number_of_incorrect_guesses == 7:
        print("""
        ______
        |
        |
        |
        |   
        """)
    elif number_of_incorrect_guesses == 8:
        print("""
        ______
        |    |
        |
        |
        |   
        """)
    elif number_of_incorrect_guesses == 9:
        print("""
        ______
        |    |
        |    O
        |
        |   
        """)     
    elif number_of_incorrect_guesses == 10:
        print("""
        ______
        |    |
        |    O
        |    |
        |   
        """)    
    elif number_of_incorrect_guesses == 11:
        print("""
        ______
        |    |
        |    O
        |   /|
        |   
        """)     
    elif number_of_incorrect_guesses == 12:
        print("""
        ______
        |    |
        |    O
        |   /|\\
        |   
        """)        
    elif number_of_incorrect_guesses == 13:
        print("""
        ______
        |    |
        |    O
        |   /|\\
        |   /
        """)        
    elif number_of_incorrect_guesses == 14:
        print("""
        ______
        |    |
        |    O
        |   /|\\
        |   / \\
        """)

#-----------------------------------------
word = get_word()
word_list = string_to_list(word)
hidden_list = ["_"]*len(word_list)
hangman_list = []

print_greetings()

while (True):
    print_list(hidden_list)
    print_list(hangman_list)
    char = get_guess()
    
    positions_list = get_position_of_guess(char,word_list)
    
    if len(positions_list) > 0:
        hidden_list = add_correct_letter(hidden_list,positions_list,char)
    else:
        hangman_list.append(char)
        print_hangman(len(hangman_list))
        if len(hangman_list) > 14:
            print("You lost, the correct word was:'", word, "'")
            break
    
    if are_we_done(word_list,hidden_list):
        print("You are a WINNER!")
        break
