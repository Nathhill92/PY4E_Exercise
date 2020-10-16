import random

#Write a function that returns 3x+1 in a traditional and lambda format
#traditional
def f(x):
    return 3*x+1
print(f(2))
print(f(5))
#lambda version
l = lambda x: 3*x+1
print(l(2))
print(l(5))

#Lambda function with more than one input
full_name = lambda fn, ln: fn.strip().title() + " " +ln.strip().title()
print(full_name("    leonhard", "EULER"))
print(full_name("RANDAL", "       Smitherson"))

#Use lambda to sort this list of sci-fi authors by last name
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arther C. Clark", "Frank Herbert", 
"Orson Scott Card", "Douglas Adams", "H.G. Wells", "Leigh Brackett"]
print(scifi_authors)
scifi_authors.sort(key=lambda name:name.split()[-1].lower())
print(scifi_authors)


print("\n\nhttps://www.w3resource.com/python-exercises/lambda/index.php Examples\n\n")
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result.
f = lambda x: x + 15
print(f(12))
print(f(3))
f2 = lambda x,y: x*y
print(f2(1,2))
print(f2(14,4))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
f3 = lambda x: x * 15
print(f3(10))
print(f3(5))
print(f3(12))

#Write a Python program to sort a list of tuples using Lambda.
list_to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(list_to_sort)
list_to_sort.sort(key= lambda x: x[1])
print(list_to_sort)

#Write a Python program to filter a list of integers for even values using Lambda
int_list = [x for x in range(1,11)]
evens = list(filter(lambda x: x%2 == 0, int_list))
odds = list(filter(lambda x: x%2 != 0, int_list))
print(evens)
print(odds)
