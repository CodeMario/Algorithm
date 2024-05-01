def solution(babbling):
    answer = 0
    for i in babbling :
        length = len(i)
        expectedLength = 0
        if 'aya' in i :
            expectedLength += 3
        if 'ye' in i :
            expectedLength += 2      
        if 'woo' in i :
            expectedLength += 3
        if 'ma' in i :
            expectedLength += 2

        if length == expectedLength :
            answer += 1

    return answer