# word_list = ["b","o","o","t","c","a","m","p"]
# hidden_list = ["_","_","_","_","_","_","_","_"]
# hangman_list = []

import random

def print_greetings():
    print("------------------------------")
    print("Hello and welcome to the game!")
    print("------------------------------")

def print_list(a_list):
    print(a_list)

def get_word():
    f = open("hangman_word_list.txt","r")
    l = f.readlines()
    lenght = len(l)
    random_number = random.randrange(0,lenght)
    word = l[random_number]
    return word[:-1]

def string_to_list(word_string):
    position = 0
    lenght = len(word_string)
    a_list = []
    while position < lenght:
        content = word_string[position]
        a_list.append(content)
        position = position + 1
    return a_list

def get_guess():
    print("Please give me a character.")
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
    return a_hidden_list

def are_we_done(a_word_list,a_hidden_list):
    if a_word_list == a_hidden_list:
        return True
    else:
        return False

#-----------------------------
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
        if len(hangman_list) > 14:
            print("You lost! The correct was", word)
            break

    if are_we_done(word_list,hidden_list):
        print(word)
        print("You are a WINNER!")
        break    