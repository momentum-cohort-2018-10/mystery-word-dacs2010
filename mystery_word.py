#import random module
import random


# open text file and build a list
with open("words.txt") as word_file:
    for word in word_file:
        # read all the lines in a file and set them to a new variable
        word_list = word_file.readlines()
        # remove all the new lines, set to upper case, and build a list
        word_list = [extra.strip().upper() for extra in word_list]
    # print(word_list)


# go through list and get a random word 
def random_word(word_list):
    '''
    random word generator
    '''
    for _ in word_list:  
        return random.choice(word_list)
# print(random_word(word_list))


#take in user input(make sure it is only one letter)
user_input = input("type a letter ").upper()
# print(user_input)


def play_game(user_input):
    '''
    take user input and check it against a random word
    '''
    game_word = random_word(word_list)
    print(game_word)
    letters = ""
    guesses = 8
    word_guessed = False
    

    while  not word_guessed  and guesses > 0:
        guess = user_input
        print(guesses)
        print(letters)
        if letters == game_word:
            word_guessed = True
        if guess in game_word:
            letters = letters + user_input
            print("good guess, try again")
        else:
            letters = letters = user_input
            guesses -= 1
            print("no good, try again")
print(play_game(user_input))