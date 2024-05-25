def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    answer = strings
    return answer