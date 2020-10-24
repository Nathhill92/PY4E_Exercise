# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
# Create a function that takes a string and applies the Atbash cipher to it.

# Examples
# atbash("apple") ➞ "zkkov"
# atbash("Hello world!") ➞ "Svool dliow!"
# atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

# Notes
# Capitalisation should be retained.
# Non-alphabetic characters should not be altered.

import string

def atbash(str):
    lower_char_list = string.ascii_lowercase
    upper_char_list = string.ascii_uppercase
    return_str = ""

    for letter in str:
        if letter in lower_char_list:
            return_str += lower_char_list[-(lower_char_list.index(letter)+1)]

        elif letter in upper_char_list:
            return_str += upper_char_list[-(upper_char_list.index(letter)+1)]
        else:
            return_str += letter
    
    print(return_str)

atbash("test")
atbash("apple")
atbash("Hello world!")
atbash("Christmas is the 25th of December")