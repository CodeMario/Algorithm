def solution(dots):
    answer = 0
    lines = [abs(dots[0][0]-dots[1][0])+abs(dots[0][1]-dots[1][1]),
            abs(dots[0][0]-dots[2][0])+abs(dots[0][1]-dots[2][1]),
            abs(dots[0][0]-dots[3][0])+abs(dots[0][1]-dots[3][1])]
    lines.sort()
    answer = lines[0]*lines[1]
    return answer