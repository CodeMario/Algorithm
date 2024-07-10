def solution(cacheSize, cities):
    answer = 0
    cities = list(map(lambda x : x.lower(), cities))
    cache = ['']*cacheSize
    for i in cities :
        if i in cache :
            answer += 1
            cache.remove(i)
            cache.append(i)
        else :
            answer += 5
            cache.append(i)
            del cache[0]
    return answer