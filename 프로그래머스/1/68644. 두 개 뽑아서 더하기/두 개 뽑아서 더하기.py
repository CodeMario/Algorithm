def solution(numbers):
    answer = set([])
    for i in range(0,len(numbers)-1) :
        for j in range(i+1,len(numbers)) :
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer