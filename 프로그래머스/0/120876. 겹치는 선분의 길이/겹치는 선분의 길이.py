def solution(lines):
    answer = []
    lines.sort(key = lambda x: x[0])
    if lines[0][1] > lines[1][0] :
        answer += range(lines[1][0],min(lines[0][1],lines[1][1]))
    
    if max(lines[0][1],lines[1][1]) > lines[2][0] :
        answer += range(lines[2][0],min(max(lines[0][1],lines[1][1]),lines[2][1]))
        
    answer = len(list(set(answer))) 
    return answer