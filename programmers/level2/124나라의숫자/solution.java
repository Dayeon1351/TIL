import java.util.*;
class Solution {
    public String solution(int n) {
        String answer = "";
     
        
        while(n!=0){
           int r = n%3==0 ? 4 : n%3;
            if(n%3==0){
                n--;
            }
            answer=Integer.toString(r).concat(answer);
            n/=3;
        }
        
        return answer;
    }
}
