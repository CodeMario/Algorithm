def solution(board, h, w):
    answer = 0
    height = len(board)
    width = len(board[0])
    color = board[h][w]
    location = [[1,0],[-1,0],[0,1],[0,-1]]
    if h == 0 :
        location.remove([-1,0])
    if h == height-1 :
        location.remove([1,0])
    
    if w == 0 :
        location.remove([0,-1])
    if w == width-1 :
        location.remove([0,1])
    
    for i in location :
        if board[h+i[0]][w+i[1]] == color :
            answer += 1
    return answer