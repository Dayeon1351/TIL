import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> al = new ArrayList<>();
        while(n!=0){
            al.add(n%3);
            n/=3;
        }
        
        int num = al.size()-1;
        for(Integer i : al){
            answer+=i*Math.pow(3,num--);
        }
        
        return answer;
    }
}
