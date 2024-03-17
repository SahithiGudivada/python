#anser:
user_word = input("enter a word: ") # Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
    letter = letter.upper()
    if letter == "A" or letter == "E" or  letter == "I" or letter == "O" or letter == "U" :
        continue
      
    else :
        print(letter,end ="") # Print the word assigned to word_without_vowels.
