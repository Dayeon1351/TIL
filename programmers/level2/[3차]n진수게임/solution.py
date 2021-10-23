def convertNum(num,base):
    string = ''
    array = ['A','B','C','D','E','F']
    
    if num == 0:
        return str(num)
    else:
        while num:
            string += str(num % base) if num % base < 10 else array[num % base % 10] 
            num = num // base

        return string[::-1]
    
def solution(n, t, m, p):
    answer = ''
    result = ''
    cnt = 0
    
    while len(result) < m*t:
        result += convertNum(cnt,n)
        cnt+=1
    
    answer = result[p-1:m*t:m]
        
    return answer
