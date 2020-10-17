def solution(x):
    return prime_str[x:x+5]

prime_str = '2'
for num in range(3,20300,2):
    prime = True
    for i in range(2,int(num/2)+1):
        if (num%i==0):
            prime = False
            break
    if prime:
       prime_str += str(num)

print(solution(0))
print(solution(8500))
print(solution(3))
print(solution(10000))