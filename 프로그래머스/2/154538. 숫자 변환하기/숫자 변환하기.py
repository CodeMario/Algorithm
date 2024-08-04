def solution(x, y, n):
    answer = -1
    cnt = 0
    queue = [y]
    if x == y :
        return 0
    while len(queue) > 0 :
        cnt += 1
        acc = []
        for i in queue :
            temp = [i-n,i/2,i/3]
            acc += [j for j in temp if j>=x and j==j//1]
        if x in acc :
            return cnt
        
        queue = acc
    return answer