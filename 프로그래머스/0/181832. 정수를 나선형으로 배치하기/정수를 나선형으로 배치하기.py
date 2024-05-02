def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    currentIndex = [0,0]
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    d = 0
    value = 2

    while answer[currentIndex[0]][currentIndex[1]] != n*n :
        y = currentIndex[0]+direction[d][0]
        x = currentIndex[1]+direction[d][1]
        if (x >= 0 and x < n) and (y >= 0 and y < n) and (answer[y][x] == 0):
            answer[y][x] = value
            value+=1
            currentIndex = [y,x]
        else :
            d = (d+1)%4
    return answer