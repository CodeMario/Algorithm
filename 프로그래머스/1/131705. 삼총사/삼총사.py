def solution(number):
    answer = 0
    temp = 0
    for i in range(len(number[:-2])) :
        temp += number[i]
        for j in range(i+1,len(number[:-1])) :
            temp += number[j]
            for k in range(j+1,len(number)) :
                temp += number[k]
                if temp == 0:
                    answer += 1
                temp -= number[k]
            temp -= number[j]
        temp -= number[i]
    return answer