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

def win_condition(letters, game_word, correct_answer):
    '''
    check the letter against the game word, if they match user wins
    '''
    while correct_answer:
        if letters == game_word:
            correct_answer = True
            print(correct_answer)
            print("YOU WIN!!!")
            break
        else:
            return False

# def change_letters_to_blanks():
#     for char in word 
        

def play_game(game_word):
    '''
    take user input and check it against a random word
    '''
    game_word = random_word(word_list)
    print(game_word) # testing purposes (replace with "_" for letters function)
    letters = ""
    guesses = 7
    correct_answer = True
    
    # (can't exit loop... HELP)
    while correct_answer is True or guesses > 0:
        guess = input("type a letter => ").upper()
        print("You have",+ guesses, "tries left ")

        # correct guess
        if guess in game_word:
            letters = letters + guess
            win_condition(letters, game_word, correct_answer)
            print("Guessed letters => " + letters)
            print("Good guess, try again \n")

        # incorrect guess
        elif guess not in game_word:
            guesses -= 1
            letters = letters + guess
            win_condition(letters, game_word, correct_answer)
            print("Guessed letters => " + letters)
            print("No good, try again \n")
        else:
            return

# call the game, the random word generator, and the word list            
print(play_game(random_word(word_list)))