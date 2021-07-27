import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = Integer.toBinaryString(n).replace("0","").length();
      
        while(cnt!=Integer.toBinaryString(n+1).replace("0","").length()){
            n++;
        }
        answer=n+1;
        
        return answer;
    }
}
