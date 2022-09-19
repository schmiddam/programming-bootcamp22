import random

def how_many_chars():
    print("Hello and welcome from Pyfonics!")
    print("We are here to give you the safest password.")
    print("How many characters should your password have?")
    number = int(input())
    return number 

def string_to_list(a_word):
    character_list = []
    position = 0
    string_to_iterate = a_word
    while position < len(string_to_iterate):
        character_list.append(string_to_iterate[position])
        position = position + 1
    return character_list

def create_password_list():
    password_list = []
    return password_list

def add_random_letter(password_list, character_list, number):
    position = 0
    while position < number:
        password_list.append(random.choice(character_list))
        position = position + 1
    return password_list

def sum_elements_list(a_list):
    position = 0
    my_sum = a_list[position]
    position = position + 1
    while position < len(a_list):
        value = a_list[position]
        my_sum = my_sum + value
        position = position + 1
    return my_sum

character_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.+*%"

password_number = how_many_chars()

char_list = string_to_list(character_string)

passwortliste = create_password_list()

neuepasswortliste = add_random_letter(passwortliste, char_list, password_number)

passwort = sum_elements_list(neuepasswortliste)
print (passwort)