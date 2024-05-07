def solution(n):
    answer = 0
    nums = []
    n -= 1
    i = 2
    while i <= n:
        if n%i == 0 :
            nums.append(i)
            n %= i
        else :
            i+=1
    answer = min(nums)
    return answer