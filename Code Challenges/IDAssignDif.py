#Charles is in charge
def solution(x):
    return prime_str[x:x+5]

prime_str = '2'
prime_count = 3


for x in range(prime_count, 10005):
    if len(prime_str) > 10005: break
    if prime_count % x == 0: continue
    
    prime_str += str(prime_count)
    prime_count += 2

#test outputs
print(solution(0))
print(solution(8500))
print(solution(3))
print(solution(10000))