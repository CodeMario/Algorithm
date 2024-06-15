def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    newBoard = [[] for i in range(n)]
    for i in range(n-1,-1,-1) :
        for j in range(n) :
            if board[i][j] != 0 :
                newBoard[j].append(board[i][j])

    for i in moves :
        if len(newBoard[i-1]) != 0 :
            stack.append(newBoard[i-1].pop())
        
        if len(stack) >= 2 :
            if stack[-1] == stack[-2] :
                answer += 2
                stack = stack[:-2]
                
    return answer