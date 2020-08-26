sentence = input("Please enter a sentence: ")
upper_first_word = sentence.title()  # Capitalized each separate word
remove_space = upper_first_word.replace(" ", "")  # removes space
# lowercase the first word then add with the rest
print(remove_space[0:1].lower() + remove_space[1:])
