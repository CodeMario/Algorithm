def solution(x):
    answer = True
    n = list(map(int,list(str(x))))
    if x % sum(n) != 0 :
        answer = False
    return answer