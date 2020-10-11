# Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).

# Examples
# char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

# char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

# char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]

def char_at_pos(input, specifier):
    print(input)
    startpos = 1
    if specifier == "even":
        startpos = 2

    return input[startpos-1::2]

print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))
print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even"))

#extra challenge:
    #Same thing from the *last* item of that list or string.

def char_at_pos_from_last(input, specifier):
    print(input)
    startpos = 1
    if specifier == "even":
        startpos = 2
    output_from_last = input[:-(startpos-1):-2]
    output_from_last.reverse()
    return output_from_last

print(char_at_pos_from_last([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd"))

#todo
    #From the exercise, this is possible with a single line lambda function. Try that when I get comfortable with single line and lambda functions