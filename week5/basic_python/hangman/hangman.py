import random

def generate_word():
    random_words = [
    "nebula", "bicycle", "quench", "whisper", "glimmer", 
    "syntax", "ocean", "velocity", "marmalade", "clover", 
    "echo", "pinnacle", "safari", "riddle", "zenith", 
    "fossil", "tundra", "labyrinth", "harvest", "spark"]

    random_num = random.randint(0,19)

    return random_words[random_num]
    
def get_guess():
    while True:
        letter = input("letter")
        if letter.isalpha():
            break
        else:
            print("please enter a letter")

    return letter
    
 