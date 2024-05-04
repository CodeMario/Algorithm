def solution(balls, share):
    answer = 1
    temp = 1
    for i in range(share) :
        answer *= (balls-i)
        temp *= (share-i)
    answer /= temp
    return answer