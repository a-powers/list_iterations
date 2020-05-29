# argv means argument variable
# go to terminal, type python, type <file>, type a few words to get the character length.  
# Hit enter.  Length is printed in terminal



import sys

word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"The total length of all command-line arguments is {word_lengths}.")