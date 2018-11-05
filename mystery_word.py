import random


# open text file and build a list
with open("words.txt") as word_file:
    for word in word_file:
        # read all the lines in a file and set them to a new variable
        word_list = word_file.readlines()
        # remove all the new lines, set to upper case, and build a list
        word_list = [extra.strip().upper() for extra in word_list]
    # print(word_list)
 

def random_word(word_list):
    '''
    random word generator
    '''
    # iterate through the word list...
    for _ in word_list:  
        # and select a random word
        return random.choice(word_list)


# snagg clintons print instructions idea
def print_instructions():
    '''
    prints the game instructions
    '''
    print(
        "try to guess the mystery word,\nyou can guess incorrectly 8 times,\ngood luck!"
        )  


def make_game_board(game_word):
    '''
    take the char in the game word and prints out a string with a "_" for each character
    '''
    game_board = []
    for _ in game_word:
        game_board.append("_")
    return game_board

# not finished
def replace_letters(guess, word, game_board):
    '''
    if guess is in word, then insert it into game board at the same index as the word "_"
    '''
    changes = game_board
    for i in word:
        if guess in word:
            changes.insert(i, guess)
            return changes


def play_game(game_word):
    '''
    take user input and check it against a random word
    '''
    game_word = random_word(word_list)
    game_board = make_game_board(game_word)
    print(game_word) # testing purposes
    print(game_board)
    answer = ""
    letters = ""
    guesses = 7
    correct_answer = False
    print_instructions()
    
    # (ok... i need to enter an extra guess to exit loop for win condition)
    while not correct_answer or guesses > 0:
        guess = input("type a letter => " + "\n").upper()
        print("You have",+ guesses, "tries left ")
        
        # win condition
        if answer == game_word:
            correct_answer = True
            print("answer" + answer) # test
            print("YOU WIN!!!")
            return

        # correct guess
        elif guess in game_word:
            # add guessed chars to the letters string
            letters = letters + guess
            answer = letters + answer
            print("answer" + answer) # test
            print("Guessed letters => " + letters)
            print("Good guess!, try another! \n")

        # incorrect guess
        else:
            # declinate for each wrong guess (not working for initial guess)
            guesses -= 1
            # add chars letters to the letters string
            letters = letters + guess
            print("Guessed letters => " + letters)
            print("No good, try again... \n")

# call the game, the random word generator, and the word list            
print(play_game(random_word(word_list)))