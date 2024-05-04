def solution(score):
    answer = [1]*len(score)
    score = list(map(sum, score))
    rank = score[:]
    rank.sort(reverse=True)
    for i in range(len(score)) :
        answer[i] += rank.index(score[i])
    return answer