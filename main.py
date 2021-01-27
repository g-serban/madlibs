# creating a madlib using string concatenation with f strings

from madlibs import madlibs

madlibs()


# Basically what we are doing here:
# importing the function madlibs from the module madlibs
# and we run it here
# what the function does:

# we ask for an input from the user. He has to choose between 3 madlibs games. If he chooses to 1, 2 or 3 he is going to 'enter' those games
# if he enters any different number, he is going to be warned that he did a mistake and is going to be asked again to enter 1 2 or 3 (this is the doing of else)

# if he presses 1 2 or 3 he is going to be asked to enter some words (pronouns, adverbs, etc.)
# after he enters all of them, he is going to get the madlib text.
# I've created the madlib using string concatenation (f"etc {etc}) where {etc} are the pronouns, adverbs, etc.

# after the game is done, the user is asked if he want to try again and has to enter yes or no
# if yes, he gets to the 'start/ main menu' again where he can try the other option or replay the previous one
# if no, the program will exit and print an exiting message
# but if he doesn't enter yes/ no, then I have a loop in place that will keep asking him for the yes or no values until he does enter the right thing

# that's kinda it, this is the first Python program that I've actually built by myseld and not by following a code along video

# and it's true that the function is pretty big and is not really a pure function (it calls things like print and input from the global scope)
# but I don't really know how to keep the variables for the madlibs games that ask for input from users outside of the function, without trigerring the input 
                                                                                                                            # (even if I don't want those inputs to be triggered rn)
# but actually thinking about it, it kinda does make sense to keep them in a function. Because after the function exits, the values are not going to be stored
# in the memory, they are going to be erased by Python's garbage collector at the end 

