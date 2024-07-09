def solution(s):
    answer = []
    s = s[:-2].split('}')
    arr = []
    for i in s :
        arr.append(list(map(int,i[2:].split(','))))
    arr.sort(key = lambda x: len(x))
    
    for i in arr :
        for j in range(len(i)) :
            if i[j] not in answer :
                answer.append(i[j])
                break
    return answer