#Join the list's elements with: "+++".

list = ["Hawaii", "Phuket", "Aruba", "Keys"]
joined = '+++'.join(list)
print(joined)
print()
#Join the tuple's elements so that you get a proper email address.
addresses=("Mr.Hathaway", "amymail.com")
#Type your code here.
email= "@".join(addresses)
print(email)
print()
#Join with a space in between
lst=['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']
#Type your code here.
str=' '.join(lst)
print(str)
print()
#Using .join() method join the keys in the dictionary with a comma: ",".
economic_growth={"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}
#Type your code here.
str=', '.join(economic_growth)
print(str)
print()
# "\n" is a character that creates a new line. (Similar to when you press enter key in your text editor.)
# Using "\n" character and .join() method, join the sentences in the list so that it looks like a proper poem.
poem_lst=["Not enjoyment, and not sorrow,", "Is our destined end or way;", "But to act, that each tomorrow", "Find us farther than today."]
#Type your code here.
poem_str="\n".join(poem_lst)
print(poem_str)