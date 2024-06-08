def solution(a, b, c, d):
    answer = 1
    num = [a,b,c,d]
    num.sort()
    temp = list(set(num))
    cnt = len(temp)
    
    if cnt == 1 :
        answer = 1111 * temp[0]
    elif cnt == 2 :
        if num[1] == num[2] :
            temp.remove(num[1])
            answer = (10*num[1]+temp[0])**2
        else :
            answer = (num[1]+num[2])*abs(num[1]-num[2])
    elif cnt == 3 :
        num.remove(temp[0])
        num.remove(temp[1])
        num.remove(temp[2])
        temp.remove(num[0])
        answer = temp[0]*temp[1]
    else :
        answer = num[0]
    
    return answer