def solution(board):
    answer = 0
    n = len(board)
    
    #인덱스 범위초과 방지를 위해 사방으로 0을 한 줄씩 추가
    for i in range(n) :
        board[i].insert(0,0)
        board[i].append(0)
    board.append([0]*(n+2))
    board.insert(0,[0]*(n+2))
    
    #인덱스가 지뢰가 아닌 경우, 해당 인덱스를 중심으로 3x3 공간안에 지뢰가 있나 검사 -> 없으면 answer + 1
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if board[i][j] != 1 :
                around = board[i-1][j-1:j+2]+board[i][j-1:j+2]+board[i+1][j-1:j+2]
                if 1 not in around :
                    answer += 1
    return answer