def solution(my_string):
    temp = my_string.split()
    answer = int(temp[0])
    for i in range(1,len(temp),2) :
        if temp[i] == "+" :
            answer += int(temp[i+1])
        else :
            answer -= int(temp[i+1])
    
    return answer