#return max
import functools
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis))
# ruber ducky walkthrough:
# reduce takes two arguments, 
#   the function logic and the list to to perform the function logic on
#   The value of returned by the logic serves as the "a" value for future iterations of this function
#   A one value bubble sort

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis))  

# return product
print ("The product of the list elements is: ",end='')
print(functools.reduce(lambda a,b: a*b,lis))

#find smallest item in list
print("The smmalles item in the lost elements is:",end="")
print(functools.reduce(lambda x,y: x if x < y else y,lis))
