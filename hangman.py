from multiprocessing.dummy import current_process
import random

words = "shave pin committee protest mainstream heaven respect precedent failure smell opposed paper translate place crutch flash frog conference koran put ex frighten plane crude innocent doubt minor looting different testify elite tired officer blame objective swim acid book judicial professional stereotype ankle visual trance rib church ride facade cool recover"
list_words = words.split()
#print(list_words)
secret_index = random.randint(0, len(list_words)-1)
#print(secret_index)
secret_word = list_words[secret_index]
#print(secret_word)
hangman={
    'secret_word': secret_word,
    'guess_word': '_' * len(secret_word),
    'lifes': 9,
}
print(f"{hangman['guess_word']}")
print(f"lifes: {hangman['lifes']}")

while True:
    letter = input("Give my your letter: ")
    if letter in hangman['secret_word'] and letter not in hangman['guess_word']:
        guess_word_letters = list(hangman['guess_word'])
        for index, current_letter in enumerate(hangman['secret_word']):
            if current_letter == letter:
                guess_word_letters[index] = letter
            hangman['guess_word'] = ''.join(guess_word_letters)
    elif letter not in hangman['secret_word']:
        hangman['lifes'] -=1
    print(f"{hangman['guess_word']}")
    print(f"lifes: {hangman['lifes']}")
    if '_' not in hangman['guess_word']:
        print('Bravo')
        break
    elif hangman['lifes']<1:
        print('Game over')
        break