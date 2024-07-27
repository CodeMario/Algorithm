def solution(dirs):
    answer = 0
    path = set()
    x1,y1 = 0,0
    move = {'U':[0,1],'D':[0,-1],
            'R':[1,0],'L':[-1,0]}
    for i in dirs :
        x2,y2 = move[i]
        if x1+x2 > 5 or x1+x2 < -5 or y1+y2 > 5 or y1+y2 < -5 :
            continue
        
        
        path.add(((x1,y1),(x1+x2,y1+y2)))
        path.add(((x1+x2,y1+y2),(x1,y1)))
        x1,y1 = x1+x2,y1+y2
    answer = len(path)//2
        
    return answer