# Create a function that takes a number and returns a string like square.
# Examples
# create_square(-1) ➞ ""
# create_square(0) ➞ ""
# create_square(1) ➞ "#"
# create_square(2) ➞ "##\n##"
# create_square(3) ➞ "###\n# #\n###"
# create_square(4) ➞ "####\n#  #\n#  #\n####"
# "####
# #  #
# #  #
# ####"

def create_square(num):
    for x in range(num):
        if x == 0 or x == num-1:
            print("# "*num)
        else:
            #the "-5" values comes from:
                # line lenth is equal to (num * 2) - 1
                # 2 are reserved for the starting and ending "#"
                # the "," characters in Python both add one space each
            print("#"," "*((2*num)-5), "#")

create_square(1)
create_square(2)
create_square(3)
create_square(5)
create_square(10)
create_square(100)
