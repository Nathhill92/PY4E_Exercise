import functools
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis))
# ruber ducky walkthrough:
# 