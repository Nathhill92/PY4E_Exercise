# Censor Words from List
# Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

# Examples
# censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
# censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
# censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

def censor_string(line, censor_list, replacement_char):
    return_str = ""
    for word in line.split():
        if word.lower() in censor_list:
            return_str += replacement_char*len(word) + " "
        else:
            return_str += word + " "
    print(return_str)

censor_string("Today is a Wednesday!", ["today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "x")