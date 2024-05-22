def solution(s, n):
    answer = ''
    for i in s :
        if i != ' ' :
            temp = ord(i) + n
            if i >= 'A' and i <= 'Z' :
                if temp > ord('Z') :
                    temp -= 26
                i = chr(temp)
            else :
                if temp > ord('z') :
                    temp -= 26
                i = chr(temp)
        answer += i
    return answer