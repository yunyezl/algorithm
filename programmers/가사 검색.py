def solution(words, queries):
    result = {}
    
    sortedQueries = sorted(queries, key = len)
    words = sorted(words, key = len)
        
    for query in sortedQueries:
        count = 0
        qCount = query.count('?')
        for word in words:
            if qCount == len(query) and len(query) == len(words):
                count += 1
                continue
            if len(query) < len(word):
                break
            elif len(query) == len(word):
                if query[0] == '?': # 접두사
                    if word[qCount:len(word)] == query[qCount:len(query)]:
                        count += 1
                else: # 접미사
                    if word[0:len(word)-qCount] == query[0:len(query)-qCount]:
                        count += 1
        result[query] = count
                    
    answer = []
    for query in queries:
        answer.append(result[query])    
    return answer
    
    # 효율성 틀림
