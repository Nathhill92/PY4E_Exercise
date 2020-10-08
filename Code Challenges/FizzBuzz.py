def fizz_buzz(test):
    outstr = ''
    if test % 3 == 0:
        outstr = 'Fizz'
    if test % 5 == 0:
        outstr += 'Buzz'
    #
    # if test % 3 != 0 and test%5 !=0:
    #     outstr = str(test)
    #
    # The "or" operator will return the "test" value if outstr is empty
    return outstr or test

for x in range(1,101):
    print(fizz_buzz(x))