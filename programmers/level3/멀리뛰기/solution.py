def solution(n):
    memo = [0,1,2,3]
    for i in range(4,n+1):
        memo.append((memo[i-1] + memo[i-2]) % 1234567)
        
    answer = memo[n]
    return answer
