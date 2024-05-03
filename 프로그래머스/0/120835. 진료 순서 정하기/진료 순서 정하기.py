def solution(emergency):
    answer = []
    rank = [i for i in emergency]
    rank.sort(reverse=True)
    for i in emergency :
        answer.append(rank.index(i)+1)
    return answer