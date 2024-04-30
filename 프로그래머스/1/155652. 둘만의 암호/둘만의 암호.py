def solution(s, skip, index):
    answer = ''
    words = list(map(chr, range(ord('a'),ord('z')+1)))
    for i in skip :
        words.remove(i)
    s= list(s)
    for i in range(len(s)) :
        newIndex = words.index(s[i]) + index
        if newIndex >= len(words) :
            s[i] = words[(newIndex%len(words))]
        else :
            s[i] = words[newIndex]
    answer = ''.join(s)
    return answer