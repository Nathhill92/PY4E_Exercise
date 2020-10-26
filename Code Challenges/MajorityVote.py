# Majority Vote
# Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# Notes
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.
from collections import Counter
import random, string

def majority_vote(votes):
    # Create Count dictionary with counts of unique values
    vote_count = Counter(votes)
    # Return highest value or None 
    for entry in vote_count:
        if vote_count[entry] > len(votes)/2:
            print(votes,"->",entry)
            return entry
    print(votes," -> None")
    return None
    
#Challenge Examples
majority_vote(["A", "A", "B"])
majority_vote(["A", "A", "A", "B", "C", "A"])
majority_vote(["A", "B", "B", "A", "C", "C"])

#Make some random lists 4 fun
#A list of uppercase letters A-Z
letterlist = string.ascii_uppercase
#Run randomized list through majority_vote
majority_vote(random.choices(letterlist, k = random.randrange(1,10)))