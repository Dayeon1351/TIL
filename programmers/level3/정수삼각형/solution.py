def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1,0,-1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
    
    answer = triangle[0][0]
    return answer
