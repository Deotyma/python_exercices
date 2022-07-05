import random

words = "shave pin committee protest mainstream heaven respect precedent failure smell opposed paper translate place crutch flash frog conference koran put ex frighten plane crude innocent doubt minor looting different testify elite tired officer blame objective swim acid book judicial professional stereotype ankle visual trance rib church ride facade cool recover"
list_words = words.split()
#print(list_words)
secret_index = random.randint(0, len(list_words)-1)
#print(secret_index)
secret_word = list_words[secret_index]
#print(secret_word)