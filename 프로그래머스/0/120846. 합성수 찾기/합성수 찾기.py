def solution(n):
    answer = 0
    temp = {}
    nums = []
    
    for i in range(1,n+1) :
        for j in range(i,n+1) :
            if j%i == 0 :
                if j in temp :
                    temp[j] += 1
                else :
                    temp[j] = 1
        if temp[i] >= 3 :
            nums.append(i)
    
    answer = len(nums)
    return answer