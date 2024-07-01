def solution(elements):
    answer = []
    n = len(elements)
    elements = elements*2
    for i in range(n) :
        for j in range(n) :
            answer.append(sum(elements[i:i+j]))
    answer = list(set(answer))
    answer = len(answer)
    return answer