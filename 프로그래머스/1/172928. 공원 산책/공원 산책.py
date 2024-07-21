def solution(park, routes):
    answer = []
    h,w = len(park),len(park[0])
    for i in range(h) :
        for j in range(w) :
            if park[i][j] == 'S' :
                cur = [i,j]
    
    for i in routes :
        d,n = i.split()
        n = int(n)
        if d == 'E' :
            if cur[1] + n >= w :
                continue
            else :
                if 'X' not in park[cur[0]][cur[1]:cur[1]+n+1] :
                    cur[1] += n
        elif d == 'W' :
            if cur[1] - n < 0 :
                continue
            else :
                if 'X' not in park[cur[0]][cur[1]-n:cur[1]+1] :
                    cur[1] -= n
        elif d == 'S' :
            if cur[0] + n >= h :
                continue
            else :
                temp = [j[cur[1]] for j in park]
                if 'X' not in temp[cur[0]:cur[0]+n+1] :
                    cur[0] += n
        else :
            if cur[0] - n < 0 :
                continue
            else :
                temp = [j[cur[1]] for j in park]
                if 'X' not in temp[cur[0]-n:cur[0]+1] :
                    cur[0] -= n
    answer = cur
    return answer