def solution(number, limit, power):
    answer = 0
    cnt = [1]*number
    for i in range(2,number+1) :
        for j in range(i,number+1,i) :
            cnt[j-1] += 1
    answer = sum(list(map(lambda x : x if x <= limit else power, cnt)))
    return answer