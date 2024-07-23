def checkPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    temp = ''    
    while n:
        temp += str(n % k)
        n //= k
    n = temp[::-1]
    n = str(n).split('0')
    n = list(map(int,' '.join(n).split()))
    
    for i in n :
        if checkPrime(i) :
            answer+=1
    
    return answer