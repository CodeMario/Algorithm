def solution(rank, attendance):
    answer = 0
    count = 3
    for i in range(1,len(rank)+1) :
        num = rank.index(i)
        if attendance[num] :
            answer += num*(10**((count-1)*2))
            count-=1
        if count == 0 :
            break
    return answer