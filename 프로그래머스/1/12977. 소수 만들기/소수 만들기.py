def prime(n) :
    temp = [True] * n
    result = []
    for i in range(n) :
        if temp[i] :
            result.append(i+2)
            for j in range(i,n,i+2) :
                temp[j] = False
    return result

def solution(nums):
    answer = 0
    nums.sort()
    l = len(nums)
    n = prime(sum(nums[-3:]))
    for i in range(0,l-2) :
        for j in range(i+1,l-1) :
            for k in range(j+1,l) :
                if (nums[i]+nums[j]+nums[k]) in n:
                    answer += 1
    return answer