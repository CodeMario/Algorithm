def solution(my_string):
    answer = ''
    my_string = list(my_string)
    answer = ''.join(list(reversed(my_string)))
    return answer