def solution(numbers, hand):
    answer = ''
    keyPad = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    leftHand = [3,0]
    rightHand = [3,2]
    for i in numbers :
        temp = keyPad.index(i)
        x = temp%3
        y = temp//3
        
        if i in [1,4,7] :
            answer += 'L'
            leftHand = [y,x]
        elif i in [3,6,9] :
            answer += 'R'
            rightHand = [y,x]
        else :
            ly = abs(leftHand[0]-y)
            lx = abs(leftHand[1]-x)
            ry = abs(rightHand[0]-y)
            rx = abs(rightHand[1]-x)

            if (ly+lx) > (ry+rx) :
                answer += 'R'
                rightHand = [y,x]

            elif (ly+lx) < (ry+rx) :
                answer += 'L'
                leftHand = [y,x]
            else :
                if hand == 'right' :
                    answer += 'R'
                    rightHand = [y,x]
                else :
                    answer += 'L'
                    leftHand = [y,x]
    return answer