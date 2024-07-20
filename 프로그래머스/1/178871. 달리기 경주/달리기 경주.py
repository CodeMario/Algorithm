def solution(players, callings):
    answer = []
    rank = {}
    for i in range(len(players)) :
        rank[players[i]] = i
    
        
    for i in callings :
        n = rank[i]
        players[n], players[n-1] = players[n-1], players[n]
        
        rank[players[n]] += 1
        rank[players[n-1]] -= 1
    
    answer = players
    return answer