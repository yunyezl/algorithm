def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for i in range(len(cities)):
        if cities[i].lower() in cache:
            answer += 1
            del cache[cache.index(cities[i].lower())]
        else:
            answer += 5
        if len(cache) < cacheSize:
            cache.append(cities[i].lower())
        elif len(cache) == cacheSize and cacheSize > 0:
            cache.pop(0)
            cache.append(cities[i].lower())

    return answer
