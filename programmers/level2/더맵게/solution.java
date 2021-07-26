import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> que = new PriorityQueue<>();
        for(Integer n : scoville){
            que.add(n);
        }
        
        while(que.peek()<K){
            if(que.size()==1){
                answer=-1;
                break;
            }
            int num = que.poll();
            que.add(num+(que.poll()*2));
            answer++;
        }
        
        return answer;
    }
}
