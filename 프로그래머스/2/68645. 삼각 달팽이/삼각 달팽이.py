#2차원 배열로 바꿔서 풀면 좋다는 힌트 보고 함
def solution(n):
    answer = []
    #방향은 3가지
    d = [1,0,0,1,-1,-1]
    y,x = 0,0
    board = [[0]*n for i in range(n)]
    i = 1
    #등차수열의 합을 이용한 마지막 값
    while i < (n+1)*n/2+1 :
        board[y][x] = i
        if y+d[0] >= n or x+d[1] >= n :
            d += d[:2]
            d = d[2:]
        elif board[y+d[0]][x+d[1]] != 0 :
            d += d[:2]
            d = d[2:]
        y,x = y+d[0],x+d[1]
        i += 1
    for i in range(n) :
        answer += board[i][:i+1]
    return answer