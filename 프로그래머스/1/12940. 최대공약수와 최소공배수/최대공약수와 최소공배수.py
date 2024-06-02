def solution(n, m):
    answer = []
    num = [n,m]
    while True :
        temp = max(num)%min(num)
        if temp == 0 :
            answer.append(min(num))
            break
        num.remove(max(num))
        num.append(temp)
    answer.append(n*m//answer[0])
    return answer