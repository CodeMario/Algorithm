def solution(polynomial):
    answer = ''
    var = 0
    const = 0
    polynomial = polynomial.split()
    for i in range(0,len(polynomial),2) :
        if polynomial[i][-1] == 'x' :
            if len(polynomial[i]) == 1 :
                var += 1
                continue
            var += int(polynomial[i][:-1])
        else :
            const += int(polynomial[i])
    if var :
        if var == 1 :
            answer += 'x'
        else :
            answer += str(var)+'x'
    if const :
        if len(answer) != 0 :
            answer += ' + '
        answer += str(const)
    return answer