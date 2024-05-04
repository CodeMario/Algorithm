def solution(sides):
    # x < min + max
    # x + min > max => x > max - min
    # max - min < x < max + min => x의 범위 == (max + min) - (max - min) - 1
    answer = min(sides)*2-1
    return answer