def solution(id_list, report, k):
    answer = [0]*len(id_list)
    acc = {}
    id_index = dict(zip(id_list,list(range(len(id_list)))))
    for i in report :
        a,b = i.split()
        if b in acc :
            acc[b].append(a)
        else :
            acc[b] = [a]
    
    for i in id_list :
        if i in acc :
            temp = list(set(acc[i]))
            if len(temp) >= k :
                for j in temp :
                    answer[id_index[j]] += 1
    
    return answer