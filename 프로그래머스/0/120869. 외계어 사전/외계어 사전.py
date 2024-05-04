def spelling(spell,dic) :
    used = []
    for i in dic :
        if i in used :
            return False
        elif i in spell :
            used.append(i)
            continue
        else :
            return False
    return True

def solution(spell, dic):
    answer = 2
    for i in dic :
        if spelling(spell,i) :
            if len(i) == len(spell) :
                answer = 1
                break
    return answer