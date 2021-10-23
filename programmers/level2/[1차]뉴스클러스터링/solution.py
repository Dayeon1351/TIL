def getUnion(strA,strB):
    result = []
    for k in list(set(strA)|set(strB)):
        result.append(max(strA.count(k),strB.count(k)))
        
    return sum(result)


def getIntersect(strA,strB):
    result = []
    for k in list(set(strA)&set(strB)):
        result.append(min(strA.count(k),strB.count(k)))
                     
    return sum(result)
                      
    
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    
    strA = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    strB = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    intersect = getIntersect(strA,strB)
    union = getUnion(strA,strB)
    
    answer = int(intersect / union * 65536) if union != 0 else 65536
    
    return answer
