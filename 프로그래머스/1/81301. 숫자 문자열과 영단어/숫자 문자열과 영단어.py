def solution(s):
    answer = ''
    temp = ''
    number = {'zero':'0','one':'1','two':'2',
              'three':'3','four':'4','five':'5',
              'six':'6','seven':'7'
              ,'eight':'8','nine':'9'}
    for i in s :
        if i >= '0' and i <= '9' :
            answer += i
        else :
            temp += i
            if temp in number :
                answer += number[temp]
                temp = ''
    answer = int(answer)
    return answer