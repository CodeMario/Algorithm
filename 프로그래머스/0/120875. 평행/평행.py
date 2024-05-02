def solution(dots):
    answer = 0
    #경우의 수는 이렇게 3개뿐임(0-1인덱스,2-3인덱스)
    couple = [[0,1,2,3],[0,2,1,3],[0,3,1,2]]

    for i in couple :
        #점 하나를 (0,0) 좌표로 이동시킨 뒤 기울기 구함
        #기울기A
        inclineA = (dots[i[0]][0]-dots[i[1]][0])/(dots[i[0]][1]-dots[i[1]][1])
        #기울기B
        inclineB = (dots[i[2]][0]-dots[i[3]][0])/(dots[i[2]][1]-dots[i[3]][1])
        
        if inclineA == inclineB :
            answer = 1
            break
    return answer