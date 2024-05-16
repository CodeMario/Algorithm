def solution(s):
    length = len(s)
    answer = s[length//2]
    if length % 2 == 0 :
        answer = s[(length//2)-1] + answer
    return answer