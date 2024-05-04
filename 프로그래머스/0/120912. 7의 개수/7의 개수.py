def solution(array):
    answer = 0
    for i in array :
        i = list(str(i))
        if '7' in i :
            for j in i :
                if j == '7' :
                    answer += 1
    return answer