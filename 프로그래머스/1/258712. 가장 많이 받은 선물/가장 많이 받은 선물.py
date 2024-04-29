def solution(friends, gifts):
    length = len(friends)
    #선물지수
    giftValue = [0]*length
    #선물 준 기록
    giftGraph = [[0 for i in range(length)] for i in range(length)]
    answer = [0]*length

    for i in range(len(gifts)) :
        #gifts의 이름을 firends리스트의 인덱스 값으로 변환
        temp = list(map(friends.index, gifts[i].split()))
        
        #준 사람 기록
        giftGraph[temp[0]][temp[1]] += 1
        #선물지수 업데이트
        giftValue[temp[0]] += 1
        giftValue[temp[1]] -= 1

    #n번째 사람이 다른 모든 사람에 대해서 선물을 받을 수 있는지 확인
    for i in range(length) :
        for k in range(length) :
            #조건에 대해 받을 수 있으면 +1
            if giftGraph[i][k] > giftGraph[k][i] :
                answer[i] += 1
            elif giftGraph[i][k] == giftGraph[k][i] and giftValue[i] > giftValue[k] :
                answer[i] += 1
    #최대값 리턴
    return max(answer)