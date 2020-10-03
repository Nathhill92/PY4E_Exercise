#Exercise 3: Use urllib to replicate the previous exercise of 
#   (1) retrieving the document from a URL, 
#   (2) displaying up to 3000 characters, and 
#   (3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.S

import urllib.request

text = urllib.request.urlopen('http://www.gutenberg.org/files/1112/1112.txt').read()

#decode and read
text = text.decode()
print(text[:3000], "\nTotal Number of Bytes:", len(text))