import re
def solution(skill, skill_trees):
    answer = 0
    # s = "|".join(list(skill))
    # for i in skill_trees:
    #     word = re.sub("[^"+s+"]","",i)
    #     if skill[:len(word)] == word:
    #         answer+=1

    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill and s != skill_list.pop(0):
                break
        else:
            answer+=1
        
    
    return answer
