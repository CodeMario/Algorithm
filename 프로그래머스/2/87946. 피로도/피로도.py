import itertools

def solution(k, dungeons):
    answer = []
    arr = list(itertools.permutations(dungeons))
    for i in range(len(arr)) :
        fatigue = k
        cnt = 0
        for j in range(len(arr[i])) :
            if arr[i][j][0] > fatigue :
                break
            elif arr[i][j][1] > fatigue :
                break
            else :
                fatigue -= arr[i][j][1]
                cnt += 1
        
        answer.append(cnt)
        
    return max(answer)