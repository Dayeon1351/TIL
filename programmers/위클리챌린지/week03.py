def solution(table, languages, preference):
    answer = ''
    result = {}
    
    for i in table:
        field = i.split()
        total = 0
        for lan,pre in zip(languages,preference):
            if lan in field:
                total += (6 - field.index(lan)) * pre
        
        if total in result.keys():
            result[total].append(field[0])
        else:
            result[total] = [field[0]]
    
    max_preference = max(result.keys())
    answer = sorted(result[max_preference])[0]
    
    return answer
