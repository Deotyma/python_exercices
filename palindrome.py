# palindrome of word
# method 1
def palindrome1 (word):
    word2 = word[::-1] #word 2 is renversed by [::–1] slice whitch starts from last letter
    print (word2)

    if word == word2:
        print(f"{word} this is a palindrom")
    else:
        print(f"{word} isn't a palindrome")  

palindrome1("kayak")  
palindrome1("tarot")
palindrome1("total")