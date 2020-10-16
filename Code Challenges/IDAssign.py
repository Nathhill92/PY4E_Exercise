def solution(x):
    return prime_str[x:x+5]

prime_str = '2'
prime_count = 3

while len(prime_str) < 10005:
    fail_count=0
    for x in range (3,int(prime_count/2)+1):
        if prime_count % x == 0:
            fail_count += 1
            break

    if fail_count == 0:
        prime_str += str(prime_count)

    prime_count += 2

#test outputs
print(solution(0))
print(solution(8500))
print(solution(3))
print(solution(10000))

