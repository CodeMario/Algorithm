import itertools

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_list = []
    for i in range(1,len(numbers)+1) :
        comb = list(set(itertools.permutations(numbers,i)))
        for j in range(len(comb)) :
            num = int(''.join(comb[j]))
            if num not in num_list :
                num_list.append(num)

    for i in num_list :
        if i == 0 or i == 1 :
            continue
        answer +=1
        for j in range(2,int(i**(1/2)+1)) :
            if i % j == 0 :
                answer -= 1
                break

    return answer