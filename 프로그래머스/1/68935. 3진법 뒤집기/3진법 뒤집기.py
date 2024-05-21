def solution(n):
    answer = 0
    three = ''
    while n // 3 != 0 :
        three += str(n%3)
        n = n//3
    three += str(n)
    answer = int(three,3)
    return answer