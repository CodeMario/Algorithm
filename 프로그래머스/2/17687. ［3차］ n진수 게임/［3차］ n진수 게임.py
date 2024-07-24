def solution(n, t, m, p):
    answer = ''
    word = dict(zip(list(range(0,16)),list(map(str,range(0,10)))+['A','B','C','D','E','F']))
    code = '0'
    i = 1
    while len(code) < t*m :
        k = i
        temp = ''
        while k :
            temp += str(word[k%n])
            k //= n
        code += temp[::-1]
        i+=1
    
    for i in range(p-1,t*m,m) :
        answer += code[i]
        
    return answer