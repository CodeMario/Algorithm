def solution(numbers):
    answer = '0'
    if sum(numbers) != 0 :
        numbers = list(map(str,numbers))
        numbers.sort(key = lambda x:(x*4))
        answer = ''.join(numbers[::-1])
    return answer