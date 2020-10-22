# Fast Fibonacci
# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:
# Fibonacci Sequence
# and
# Fibonacci Sequence 2
# for n > 1
# The beginning of the sequence is thus:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.
# Examples
# fib_fast(5) ➞ 5
# fib_fast(10) ➞ 55
# fib_fast(20) ➞ 6765
# fib_fast(50) ➞ 12586269025
# Notes
# The input number is always positive.
# You have to make it Fast.
def fibonacci_sequence():
    fib_seq = [0,1]
    for i in range (1,100):
        next = fib_seq[i-1] + fib_seq[i] 
        fib_seq.append(next)
    return fib_seq

def fast_fib(x):
    print(fib_seq[x])

fib_seq = fibonacci_sequence()
fast_fib(5)
fast_fib(10)
fast_fib(20)
fast_fib(50)