def solution(keyinput, board):
    answer = [0,0]
    board = [board[0]//2,board[1]//2]
    command = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    for i in keyinput :
        answer[0] += command[i][0]
        answer[1] += command[i][1]
        if abs(answer[0]) > board[0] or abs(answer[1]) > board[1] :
            answer[0] -= command[i][0]
            answer[1] -= command[i][1]
    return answer