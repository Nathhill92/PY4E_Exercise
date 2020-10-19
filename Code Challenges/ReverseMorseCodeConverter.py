# Encode Morse
# Create a function that takes a string as an argument and returns the Morse code equivalent.
# Examples
# encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
# encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

#create inverse of char_to_dots with dictionary comprehension
dots_to_chars = {value:key for key,value in char_to_dots.items()}


def encode_morse(pass_str):
    return_str = ""
    for letter in pass_str.upper():
        return_str += char_to_dots[letter] + " "
    
    return return_str

def decode_morse(pass_str):
    pass_str = pass_str.split(" ")
    print(pass_str)
    return_str = ""
    
    for morse_letter in pass_str:
        if morse_letter == '':
            return_str += " "
        else:
            return_str += dots_to_chars[morse_letter]

    return return_str

#print("Hello there friend! ->",encode_morse("Hello there friend!"))
#print("EDABBIT CHALLENGE ->",encode_morse("EDABBIT CHALLENGE"))
print(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. . ->",decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."))