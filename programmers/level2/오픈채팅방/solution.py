def solution(record):
    answer = []
    dic = {}
    printer = {'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}

    for i in record:
        order, info = i.split(maxsplit=1)
        if order != 'Leave':
            uid, name = info.split()
            dic[uid] = name
        
    
    for i in record:
        order, uid = i.split(maxsplit=1)
        if order != 'Change':
            answer.append(dic[uid.split()[0]] + printer[order])
    
    
    return answer
