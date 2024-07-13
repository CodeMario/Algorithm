def solution(s):
    answer = 0
    n = len(s)
    pair = {'{':'}','[':']','(':')'}
    
    if n%2==0 :
        for _ in range(n) :
            stack = []
            s += s[0]
            s = s[1:]
            for i in s :
                if i in pair :
                    stack.append(i)
                else :
                    if len(stack) == 0 :
                        continue
                    elif pair[stack[-1]] == i :
                        stack.pop()
                    else :
                        continue
            if len(stack) != 0 :
                continue
            answer += 1
        
    return answer