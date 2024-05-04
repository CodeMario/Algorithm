def solution(A, B):
    answer = 0
    count = 0
    for i in range(len(A)+1) :
        if A == B :
            answer = count
            break
        else :
            count += 1
            A = A[-1]+A[:-1]
    if count > len(A) :
        answer = -1
    return answer