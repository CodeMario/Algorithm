def solution(a, b):
    answer = 1
    num = 2
    while True :
        if b % num == 0 :
            if num == 2 or num == 5 :
                b /= num
            else :
                if a % num != 0 :
                    answer = 2
                    break
                else :
                    a /= num
                    b /= num
            
            if b == 1 :
                break
        else :
            num += 1
    return answer