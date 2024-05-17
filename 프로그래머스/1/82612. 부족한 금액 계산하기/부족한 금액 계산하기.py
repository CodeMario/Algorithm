def solution(price, money, count):
    answer = 0
    answer = ((((count**2)+count)//2)*price)-money
    if answer < 0 :
        answer = 0

    return answer