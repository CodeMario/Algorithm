def solution(s):
    answer = 0
    stack = []
    for i in s :
        stack.append(i)
        while len(stack) > 1 :
            if stack[-1] == stack[-2] :
                stack.pop()
                stack.pop()
            else :
                break
    
    if len(stack) == 0 :
        answer = 1
    return answer