def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split('.')))
    n = []
    for i in range(len(terms)) :
        temp = terms[i].split()
        n.append(int(temp[1]))
        terms[i] = temp[0]
    terms = dict(zip(terms,n))
    
    for i in range(len(privacies)) :
        temp = privacies[i]
        predict = list(map(int,[temp[:4],temp[5:7],temp[8:10]]))
        predict[1] += terms[temp[-1]]

        
        if predict[1] > 12 :
            predict[0] += predict[1]//12
            predict[1] = predict[1]%12
            if predict[1] == 0 :
                predict[0] -= 1
                predict[1] = 12
        
        if predict[0] < today[0] :
            answer.append(i+1)
            
        elif predict[0] == today[0] :
            if predict[1] < today[1] :
                answer.append(i+1)
                
            elif predict[1] == today[1] :
                if predict[2] <= today[2] :
                    answer.append(i+1)
        
    return answer