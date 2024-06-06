def solution(n):
    answer = 0
    prime = [1] * n
    prime[0] = 0
    for i in range(2,n+1) :
        for j in range(i*2,n+1,i) :
            prime[j-1] = 0
    answer = sum(prime)
    return answer