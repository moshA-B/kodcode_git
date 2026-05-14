import random

#returns a random word out of the list
def generate_word():
    random_words = [
    "nebula", "bicycle", "quench", "whisper", "glimmer", 
    "syntax", "ocean", "velocity", "marmalade", "clover", 
    "echo", "pinnacle", "safari", "riddle", "zenith", 
    "fossil", "tundra", "labyrinth", "harvest", "spark"]

    random_num = random.randint(0,19)

    return random_words[random_num]
    
#takes a guess input and validates it
def get_guess():
    while True:
        letter = input("guess a letter: ").lower()
        if not letter.isalpha() or len(letter) > 1:
            print("please enter one letter")
        else:
            break

    return letter
    
#checks if letter is in secret word
def check_in_word(word: str,letter: str):
    return letter in word

#finds the index of the guessed letter
def find_letter_index(word,letter):
    line = [i for i in range(len(word))if word[i] == letter]
    return line

#builds visual of guessed letters and remaining slots
def show_visual(word, list_of_indics):
    visual_str = ""
    for i in range(len(word)):
        if i in list_of_indics:
            visual_str +=f" {word[i]} "
        else:
            visual_str += " _ "
    return visual_str

#prints the game status
def show_status(current_visual: str, guesses_left: int, wrong_letters: list[str] ):
    print(current_visual)
    print(f"number of guesses left: {guesses_left}")
    print(f"letters guessed wrong: {wrong_letters}")
    return

#self explanatory
def check_if_in_list(the_list:list, item):
    for i in item:
        if not i in the_list:
            the_list.append(i)
    return

def game_over(list_of_indics, word, remaining_guesses):
    if len(list_of_indics) == len(word):
        print(f"you win!!! the word was {word} ")
        print(r"""
 __      __.__                              
/  \    /  \__| ____   ____   ___________  
\   \/\/   /  |/    \ /    \_/ __ \_  __ \ 
 \        /|  |   |  \   |  \  ___/|  | \/ 
  \__/\  / |__|___|  /___|  /\___  >__|    
       \/          \/     \/     \/        
""")
        return True
    elif remaining_guesses == 0:
        print(f"the word was {word}")
        print(r"""
.____    ________    _________________ __________ 
|    |   \_____  \  /   _____/\_   ___ \\______   \
|    |    /   |   \ \_____  \ /    \  \/ |       _/
|    |___/    |    \/        \\     \____|    |   \
|_______ \_______  /_______  / \______  /|____|_  /
        \/       \/        \/         \/        \/ 
""")
        return True
    else:
        return False
        
        
def main():
    remaining_guesses = 10
    secret_word = generate_word()
    missed_guesses = []
    reveled_indics = []
    while remaining_guesses > 0:
        current_visual = show_visual(secret_word, reveled_indics)
        show_status(current_visual, remaining_guesses, missed_guesses)
        guess = get_guess()
    
        if not check_in_word(secret_word, guess):
            remaining_guesses -= 1
            check_if_in_list(missed_guesses, guess)
            print("not in word")
        else:
            print("good guess")
            good_guess = find_letter_index(secret_word, guess)
            check_if_in_list(reveled_indics, good_guess)
            
        if game_over(reveled_indics,secret_word,remaining_guesses):
            break
        continue
            
    
    

if __name__ == "__main__":
    main()


