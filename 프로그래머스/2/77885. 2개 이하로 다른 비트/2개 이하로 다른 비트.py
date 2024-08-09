def solution(numbers):
    answer = []
    for i in numbers :
        flag = True
        n = bin(i)[2:]
        for j in range(len(n)-1,-1,-1) :
            if n[j] == '0' :
                if j != len(n)-1 :
                    last = '10'+n[j+2:]
                else :
                    last = '1'+n[j+1:]
                n = n[:j]+last
                flag = False
                break
        if flag :
            n = '10'+n[1:]
        answer.append(int(n,2))
    return answer