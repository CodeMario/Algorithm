def solution(a, b):
    answer = ''
    week = ['FRI','SAT','SUN','MON',
            'TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30]
    answer = week[(sum(month[:a-1])+b-1)%7]
    return answer